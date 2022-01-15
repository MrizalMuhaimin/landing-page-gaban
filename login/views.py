from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

from .forms import LoginForm


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

def loginView(request):
    cekEmail = EmailBackend()

    context = {
        'allFormField':LoginForm(),
        
    }

    if request.user.is_authenticated:
        print("User is logged")
        return redirect('/dashboard')

    user = None
    if request.method == "POST":
        username_login = request.POST['email_field']
        password_login = request.POST['password_field']
        checklist_login = request.POST['check_field']
        

        user = cekEmail.authenticate(request, username=username_login, password=password_login)
        print(user, checklist_login)
        
        if user is not None:
            request.session.set_expiry(900)
            login(request, user)
            
            return redirect('/dashboard')
        else:
            return redirect('/login')

    return render(request,"login.html",context)