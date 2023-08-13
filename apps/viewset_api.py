from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import *


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer


@api_view(['GET'])
def get_member_by_phone(request, phone):
    try:
        member = Members.objects.get(phone=phone)
        serializer = MemberSerializer(member)
        return Response(serializer.data)
    except Members.DoesNotExist:
        return Response({})


class MemberDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    lookup_field = 'phone'

    def get_queryset(self):
        return Members.objects.filter(phone=self.kwargs['phone'])
