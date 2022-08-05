from django import views
from django.contrib import admin
from django.urls import path,include
from consumables.views import ItemView,NewItemView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("items", ItemView)
# router.register("delete",DeletedItemView)
# router.register("count",CountView,basename="count")
# router.register("newitem",NewItemView)

# router.register("newitem/$",NewItemView,basename="newitem")

urlpatterns = [
    path('',include(router.urls)),
    path('delete/<int:pk>',views.DeletedItemView, name='DeletedItemView'),
    path('newitem/<int:pk>',NewItemView.as_view({'get': 'list'})),
    path('newitem/',NewItemView.as_view({'post': 'create'})),
    path('newitem/<int:pk>',NewItemView.as_view({'delete': 'destroy'}))
]
