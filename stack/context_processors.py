from stack.models  import Questions,Answers,Userprofile


def Actvts(request):

     if request.user.is_authenticated:
        cnt= Questions.objects.filter(user=request.user).count()
        ancnt= Answers.objects.filter(user=request.user).count()

        return {"qcnt":cnt,"acnt":ancnt}
     else:
        return {"qcnt":0}