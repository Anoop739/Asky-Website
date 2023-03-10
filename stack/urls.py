from django.urls import path
from stack import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("register",views.SignupView.as_view(),name="register"),
    path("login",views.SigninView.as_view(),name="login"),
    path("home",views.IndexView.as_view(),name="index"),
    path("questions/<int:id>/aswers/add",views.AddanswerView.as_view(),name="addanswer"),
    path("answers/<int:id>/upvote/add",views.UpvoteView.as_view(),name="up_vote"),
    path("profile/add",views.UserprofileView.as_view(),name="profile-add"),
    path("profile/detail",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profile/change/<int:id>",views.UserprofileEditView.as_view(),name="profile-edit"),
    path("qstns/remove/<int:id>",views.QnDeleteView.as_view(),name="qstns-remo"),
    path("answers/<int:id>/upvote/remove",views.UpvoteremoveView.as_view(),name="up_vote-remove"),
    path("ans/remove/<int:id>",views.AnsDeleteView.as_view(),name="ans-remo"),
    path("logout",views.SignoutView.as_view(),name="signout"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)