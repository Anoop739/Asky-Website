from django.shortcuts import render
from django.contrib.auth.models import User
from stack.models import Userprofile,Questions,Answers

# Create your views here.
from api.serializers import Userserializers,Profileserializers,Qustionserializer,Answerserializer
from rest_framework.viewsets import  ModelViewSet,ViewSet,GenericViewSet
from rest_framework.response import  Response
from rest_framework.decorators import  action
from rest_framework.mixins import CreateModelMixin
from rest_framework import  authentication,permissions
from rest_framework import serializers

from rest_framework.generics import GenericAPIView



# class UserView(ViewSet):
#      def create(self,request,*args,**kw):
#         serializer=Userserializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:     
#             return Response(data=serializer.errors)
class UserView(GenericViewSet,CreateModelMixin):
  #  authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=Userserializers
    queryset=User.objects.all()

class ProfileView(ModelViewSet):
    serializer_class=Profileserializers
    queryset=Userprofile.objects.all()
   # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]




    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    # def get_queryset(self):
    #   return Userprofile.objects.filter(user=self.request.user)


    def destroy(self, request, *args, **kwargs):
        pro=self.get_object
        if pro.user !=request.user:
         raise serializers.ValidationError("not allowed")
        else:
            return super().destroy(request,*args,**kwargs)
    



    # def list(self, request, *args, **kwargs):
    #     qs-=Userprofile.objects.get(user=request.user)
    #     serializer=Profileserializers(qs,many=False)
    #     return Response(data=serializer.data)
    # def create(self,request,*args,**kw):
    #      serializer=Profileserializers(data=request.data)
    #      if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(data=serializer.data)
    #      else:     
    #         return Response(data=serializer.errors)
class QuestionsView(ModelViewSet):
    serializer_class=Qustionserializer
    queryset=Questions.objects.all()
 #   authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def get_queryset(self):
    #  return Questions.objects.all().order_by("created_date")
@action (methods="post" ,detail=True)
def add_answer(self,request,*args,**kwargs):
    serializer=Answerserializer(data=request.data)
   
    ques=self.get_object()
    usr=request.user
    if serializer.is_valid():
        serializer.save(questions=ques,user=usr)
        return Response(data=serializer.data)
    else:
       return Response(data=serializer.errors)
    

class AnswerView(ModelViewSet):
    serializer_class=Answerserializer
    queryset=Answers.objects.all()
   #
   #  authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    


    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError   ("method not allowed")
    @action (methods=["post"],detail=True)
    def add_upvote(self,request,*args,**kw):
        answer=self.get_object()
        answer.up_vote.add(request.user)
        answer.save()
        return Response(data="upvoted")
    
    @action (methods=["post"],detail=True)
    def downvote(self,request,*args,**kw):
        answer=self.get_object()
        # aid=kw.get("id")
        # answer=Questions.objects.get(id=aid)
        answer.up_vote.remove(request.user)
        answer.save()
        return Response(data="downvoted")