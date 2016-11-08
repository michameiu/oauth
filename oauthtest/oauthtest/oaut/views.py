from django.shortcuts import render
from oauthtest.oaut.models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from oauthtest.oaut.models import *
from django.db.models import Q
# Create your views here.

class ListCreateEnvelope(generics.ListCreateAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = (IsEditor,IsAuthenticated)

    def get_queryset(self):
        user=self.request.user
        return Envelope.objects.filter(Q(editors__id=user.id)| Q(owner=user)).distinct()


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Envelope.objects.all()
    serializer_class = EnvelopeSerializer
    permission_classes = (IsEditor,)


class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

