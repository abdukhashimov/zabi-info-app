from info.models import Info
from info.serializers import InfoSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class InfoListApiView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [AllowAny, ]


class InfoCreateApiView(CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAdminUser, ]

class InfoDetailUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsAdminUser, ]
