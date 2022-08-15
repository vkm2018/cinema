from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.cinema.views import CategoryView, CinemaView, CommentView, FavoriteView

router = DefaultRouter()
router.register('category', CategoryView)
router.register('comment', CommentView)
router.register('favorite', FavoriteView)
router.register('', CinemaView)



urlpatterns=[

    path('', include(router.urls)),
    # path('favorites/', FavoriteView.as_view()),
]
