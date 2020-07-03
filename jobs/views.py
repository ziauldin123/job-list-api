from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Job
from .serializers import JobSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


# class ContactList(ListCreateAPIView):

#     serializer_class = ContactSerializer
#     permission_classes = (permissions.IsAuthenticated,)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

#     def get_queryset(self):
#         return Contact.objects.filter(owner=self.request.user)


# class ContactDetailView(RetrieveUpdateDestroyAPIView):

#     serializer_class = ContactSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     lookup_field = "id"

#     def get_queryset(self):
#         return Contact.objects.filter(owner=self.request.user)

class JobList(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    
    # permission_classes = (permissions.IsAuthenticated,)

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)

    # def get_queryset(self):
    #     # return Job.objects.filter(self)
        # return Job.objects.all()


class JobDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = JobSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Job.objects.all()
        # self.serializer_class.Meta.model.objects.all()

class JobTypeView(generics.ListAPIView):
    serializer_class=JobSerializer
    queryset = Job.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
