from django.urls import path
from info.views import (
    InfoListApiView,
    InfoCreateApiView,
    InfoDetailApiView,
    InfoEditApiView,
)

urlpatterns = [
    path('info/', InfoListApiView.as_view(), name='info-list'),
    path('info/<int:pk>/', InfoDetailApiView.as_view(), name='info-detail'),
    path('info/<int:pk>/edit/', InfoEditApiView.as_view(), name='info-edit'),
    path('info/create/', InfoCreateApiView.as_view(), name='info-create'),
]
