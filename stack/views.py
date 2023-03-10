from django.shortcuts import render,redirect
from stack.forms import RegistrationForm,LoginForm,QuestionForm,UserCreationForm,UserprofileForm
from django.views.generic import View,CreateView,DeleteView,DetailView,UpdateView,ListView,TemplateView,FormView,RedirectView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from stack.models  import Questions,Answers,Userprofile
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return fn(request, *args, **kwargs)
    return wrapper
decs=[signin_required,never_cache]

class SignupView(CreateView):

    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("login")
    # def get(self,request,*args,**kwargs):
    #     form=RegistrationForm()
    #     return render(request,"register.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=RegistrationForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return redirect("register")

    #     else:
    #         return render(request,"register.html",{"form":form})
class SigninView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request, *args, **kwargs) :
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render(request,"login.html",{"form":self.form_class})

@method_decorator(decs,name="dispatch")
class IndexView(CreateView,ListView):
     model=Questions
     form_class=QuestionForm

     template_name="index.html"
     success_url=reverse_lazy("index")
     context_object_name="questions"

     def form_valid(self, form):
         form.instance.user=self.request.user
         return super().form_valid(form) 
     
     def get_queryset(self):
         return Questions.objects.all().order_by("-created_date")

@method_decorator(decs,name="dispatch")   
class AddanswerView(View):
    def post(self,request, *args, **kwargs):
        qid=kwargs.get("id")
        qstn=Questions.objects.get(id=qid)
        ans=request.POST.get("answer")
        usr=request.user
        Answers.objects.create(user=usr,question=qstn,answer=ans)
        return redirect("index")


@method_decorator(decs,name="dispatch")
class UpvoteView(View):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("id")
        ans=Answers.objects.get(id=id)
        ans.up_vote.add(request.user)
        ans.save()
        return redirect("index")

@method_decorator(decs,name="dispatch")
class UserprofileView(CreateView):
     model=Userprofile
     form_class=UserprofileForm
     template_name="profile-add.html"
     success_url=reverse_lazy("index")
     def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(decs,name="dispatch")
class ProfileDetailView(TemplateView):
    template_name="profile-detail.html"

@method_decorator(decs,name="dispatch")
class UserprofileEditView(UpdateView):
     model=Userprofile
     form_class=UserprofileForm
     template_name="profile-edit.html"
     success_url=reverse_lazy("index")
     pk_url_kwarg="id"

@method_decorator(decs,name="dispatch")
class QnDeleteView(View):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("id")
        Questions.objects.get(id=id).delete
        return redirect("index")

@method_decorator(decs,name="dispatch")
class UpvoteremoveView(View):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("id")
        ans=Answers.objects.get(id=id)
        ans.up_vote.remove(request.user)
        ans.save()
        return redirect("index")

@method_decorator(decs,name="dispatch")
class AnsDeleteView(View):
    def get(self,request, *args, **kwargs):
        id=kwargs.get("id")
        Answers.objects.get(id=id).delete
        return redirect("index")

@method_decorator(decs,name="dispatch")
class SignoutView(View):
    def get(self,request, *args, **kwargs):
     logout(request)
     return redirect("login")


    