from django.contrib import admin
from django.urls import path
from .views import get_index_page, get_article_details


urlpatterns = [
    path('/article', get_index_page),
    path('/article/<int:pk>', get_article_details)
]
