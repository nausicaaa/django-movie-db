from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.movie_db import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, base_name='movie')
router.register(r'comments', views.CommentViewSet, base_name='comment')

urlpatterns = [
    url(r'^', include(router.urls)),
    # auth not implemented, this will be useful when permissions are added
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
