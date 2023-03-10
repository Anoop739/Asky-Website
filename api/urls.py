
from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView)

#from  rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("users",views.UserView,basename="users")
router.register("profile",views.ProfileView,basename="profile")
router.register("questions",views.QuestionsView,basename="questions")
router.register("answers",views.AnswerView,basename="answers")

urlpatterns = [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
  #  path('token/',ObtainAuthToken.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls


 #"7f1995feba96675b9145ba77f77158d60853fba7"
 
 # "token": "48d12a2047650ed0712ddfea7fd9b36b71d6d070"


 
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODM0MzI3MCwiaWF0IjoxNjc4MjU2ODcwLCJqdGkiOiJmZTE2YTc0MDczZDU0NDNhOWY2ZjM3OGM1Zjg2YzlhZSIsInVzZXJfaWQiOjd9.ZOOYkcfEQUAOQ9dXOSn8a2dQt31XWHY09HXEJcyOCD8",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MjU3MTcwLCJpYXQiOjE2NzgyNTY4NzAsImp0aSI6IjAyMmNiNGQ2NjIzNTRjMTI5YzExZTViOWNlNjdjOThhIiwidXNlcl9pZCI6N30.FvS3JJnvJh07iP0L99RQLJVs3IAsKEdN47mNf3o85j4"
