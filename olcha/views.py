from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from olcha.models import Category, Group, Product, Image, User
from olcha.serializers import GroupModelSerializer, CategoryModelSerializer
from rest_framework import generics, permissions
from .serializers import ProductSerializer, ImageSerializer, UserSerializer
from olcha.permissions import IsOwnerOrReadOnly


# Create your views here.

# class CategoryListView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializers = CategoryModelSerializer(categories, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializers = CategoryModelSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# class CategoryDetailView(APIView):
#     def get_object(self, slug):
#         try:
#             return Category.objects.get(slug=slug)
#         except Category.DoesNotExist:
#             return None

#     def get(self, request, slug):
#         category = get_object_or_404(Category, slug=slug)
#         serializers = CategoryModelSerializer(category)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def put(self, request, slug):
#         category = self.get_object(slug)
#         serializer = CategoryModelSerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         category = self.get_object(slug=slug)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class GroupListView(APIView):
#     def get(self, request):
#         groups = Group.objects.all()
#         serializers = GroupModelSerializer(instance=groups, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializers = GroupModelSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    



# class GroupView(APIView):
#     def get_object(self, slug):
#         try:
#             return Group.objects.get(slug=slug)
#         except Group.DoesNotExist:
#             return None

#     def get(self, request, slug):
#         group = get_object_or_404(Group, slug=slug)
#         serializers = GroupModelSerializer(group)
#         return Response(serializers.data, status=status.HTTP_200_OK)

#     def put(self, request, slug):
#         group = self.get_object(slug)
#         serializer = GroupModelSerializer(group, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, slug):
#         group = self.get_object(slug=slug)
#         group.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
    



class CategoryListApiView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializers = CategoryModelSerializer(categories, many=True, context = {'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)


class GruopListApiView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializers = GroupModelSerializer(groups, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

class ProductListApiView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class ImageListApiView(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializers = ImageSerializer(images, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)       



class UserListApiView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailApiView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]