from django.urls import path
from info.views import (
    InfoListApiView,
    InfoCreateApiView,
    InfoDetailUpdateDeleteApiView
)

urlpatterns = [
    path('info/', InfoListApiView.as_view(), name='info-list'),
    path('info/<int:pk>/', InfoDetailUpdateDeleteApiView.as_view(), name='info-detail'),
    path('info/create/', InfoCreateApiView.as_view(), name='info-create'),
]
