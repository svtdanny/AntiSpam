from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import LearningSettings, ClassSettings, MailLists
from .permissions import IsOwner, IsAuthenticated
from .serializers import LearningSettingsSerializer, ClassSettingsSerializer, MailListsSerializer


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

class get_post_mail_lists(ListCreateAPIView):
    serializer_class = MailListsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get(self, request):
        lists = MailLists.objects.get(creator=request.user)
        
        serializer = self.serializer_class(lists)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        #MailLists.objects.filter(creator=request.user).delete()
        try:
            print(1)
            lists = MailLists.objects.get(creator=request.user)
            print(3)
        except MailLists.DoesNotExist:
            print(2)
            lists = MailLists(whiteList="", blackList="", creator=request.user)
    
        #print(lists)
        if lists.whiteList != "":
            whList = lists.whiteList
            whList = whList.split(',')
        else:
            whList = []
        
        print(lists.blackList)
        print(lists.whiteList)
        
        print(lists.blackList == '')
        if lists.blackList != "":
            blList = lists.blackList
            blList = blList.split(',')
        else:
            blList = []

        print('LLLLLIIIIIISSSSTTTTTTSSSS')
        print(whList, blList)
        print(whList)
        if request.data['whiteList'] != '':
            for el in request.data['whiteList'].split(','):
                whList.append(el)

        if request.data['blackList'] != '':
            for el in request.data['blackList'].split(','):
                blList.append(el)

        lists.whiteList = ','.join(whList)
        lists.blackList = ','.join(blList)

        lists.save()

        print(request.data)
        serializer = MailListsSerializer(lists)
       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        lists = MailLists.objects.get(creator=request.user)

        whList = lists.whiteList.split(',')
        blList = lists.blackList.split(',')

        emailsToDelete = request.data['emailsToDelete'].split(',')

        whList = [addr for addr in whList if addr not in emailsToDelete]
        blList = [addr for addr in blList if addr not in emailsToDelete]

        lists.whiteList = ','.join(whList)
        lists.blackList = ','.join(blList)

        lists.save()
        
        serializer = MailListsSerializer(lists)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
