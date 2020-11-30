from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import LearningSettings, ClassSettings
from .permissions import IsOwner, IsAuthenticated
from .serializers import LearningSettingsSerializer, ClassSettingsSerializer


# Create your views here.
class get_post_learning_sets(ListCreateAPIView):
    serializer_class = LearningSettingsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request):
        settings = LearningSettings.objects.get(creator=request.user)
       
        serializer = self.serializer_class(settings)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            settings = LearningSettings.objects.get(creator=request.user)
        except LearningSettings.DoesNotExist:
            settings = None

        serializer = LearningSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
class get_post_class_sets(ListCreateAPIView):
    serializer_class = ClassSettingsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request):
        settings = ClassSettings.objects.get(creator=request.user)
        
        serializer = self.serializer_class(settings)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            settings = ClassSettings.objects.get(creator=request.user)
        except ClassSettings.DoesNotExist:
            settings = None

        serializer = ClassSettingsSerializer(settings, data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)