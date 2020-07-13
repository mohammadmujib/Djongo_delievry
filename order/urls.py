from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateMember.as_view(), name='member_list'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMember.as_view(),
         name='member_details'),
    path('<int:member_pk>/orders/',
         views.ListCreateOrder.as_view(), name='orders_list'),
    path('<int:member_pk>orders/<int:pk>/',
         views.RetrieveUpdateDestroyOrder.as_view(), name='orders_details'),
    path('track',
         views.ListCreateTrack.as_view(), name='track_list'),
    path('track/<int:pk>/', views.RetrieveUpdateDestroyTrack.as_view(),
         name='track_details'),

]
