from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.cinema.models import Category, Cinema, Like, Rating
from applications.cinema.permissions import CustomIsAdmin
from applications.cinema.serializers import CategorySerializer, CinemaSerializer, RatingSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomIsAdmin]


class CinemaView(ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['janr']
    ordering_fields = ['id']
    search_fields = ['title']

    @action(methods=['POST'], detail=True)
    def like(self, request,pk,*args,**kwargs):
        print(request)
        print(pk)
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, cinema_id=pk)

            like_object.like = not like_object.like
            like_object.save()
            status = 'liked'
            if like_object.like:
                return Response({'status': status})
            status = 'unliked'
            return Response({'status': status})
        except:
            return Response('Нет такого продукта')

    @action(methods=['POST'], detail=True)
    def rating(self,request,pk,*args,**kwargs):


            rating_obj, _ = Rating.objects.get_or_create(owner = request.user, cinema_id=pk)
            serializer = RatingSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            rating_obj.rating = request.data['rating']
            rating_obj.save()
            return Response(request.data, status=201)






