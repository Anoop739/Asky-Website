from django.contrib.auth.models import User
from rest_framework import serializers
from stack.models import Userprofile,Questions,Answers

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class Profileserializers(serializers.ModelSerializer):
    user=Userserializers(read_only=True,many=False)
    qstns_count=serializers.CharField(read_only=True)

    class Meta:
        model=Userprofile
        fields="__all__"


class Answerserializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    upvote_count=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields=["answer","id","user","created_date","upvote_count"]

class Qustionserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    question_answers=Answerserializer(read_only=True,many=True)

    class Meta:
        model=Questions
        fields=["description","id","image","user","created_date","question_answers"]
