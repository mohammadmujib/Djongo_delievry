
# views
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . serializers import MemberSerializer, OrderSerializer, TrackSerializer


class ListCreateMember(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer


class RetrieveUpdateDestroyMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer


class ListCreateOrder(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.queryset.filter(member_id=self.kwargs.get('member_pk'))

    def perform_create(self, serializer):
        member = get_object_or_404(models.Member,
                                   pk=self.kwargs.get('member_pk'))
        serializer.save(member=member)


class RetrieveUpdateDestroyOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(),
                                 member_id=self.kwargs.get('member_pk'),
                                 pk=self.kwargs.get('pk'))


class ListCreateTrack(generics.ListCreateAPIView):
    queryset = models.Track.objects.all()
    serializer_class = TrackSerializer


class RetrieveUpdateDestroyTrack(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Track.objects.all()
    serializer_class = TrackSerializer
