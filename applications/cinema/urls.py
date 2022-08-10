from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.cinema.views import CategoryView, CinemaView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('', CinemaView)



urlpatterns=[

    path('', include(router.urls)),
]
