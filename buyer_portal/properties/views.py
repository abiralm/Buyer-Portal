from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Property, Favourite
from .serializers import PropertySerializer, FavouriteSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def favourite_list_create(request):
    if request.method == 'GET':
        favourites = Favourite.objects.filter(user=request.user)
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FavouriteSerializer(data=request.data)
        if serializer.is_valid():
            # Prevent duplicates
            property_obj = serializer.validated_data['property']
            if Favourite.objects.filter(user=request.user, property=property_obj).exists():
                return Response(
                    {'error': 'Already in favourites'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def favourite_delete(request, pk):
    try:
        favourite = Favourite.objects.get(pk=pk, user=request.user)
    except Favourite.DoesNotExist:
        return Response(
            {'error': 'Favourite not found or not yours'},
            status=status.HTTP_404_NOT_FOUND
        )
    favourite.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)