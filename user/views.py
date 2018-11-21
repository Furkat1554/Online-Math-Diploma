from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import logout
from subject.models import Subject

from .forms import *


def profile(req):
    return render(req, "profile.html")


def register_user(req):
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        profile_form = ProfileForm(req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.profile.student_grade = profile_form.cleaned_data.get('student_grade')
            user.save()

            # encrypt and password
            user_pswd = User.objects.get(username=user.username)
            user_pswd.set_password(user.password)
            user_pswd.save()

            print('successfylly registered')
            return redirect('users:profile')
        else:
            print('Please correct the error below.')
    else:
        user_form = UserForm(instance=req.user)
        profile_form = ProfileForm(instance=req.user.profile)
        print('not post')
    return render(req, 'index.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def sign_up(req):
    user_form = UserForm()
    profile_form = ProfileForm()
    register_form = RegisterForm()
    data = {
        "user_form": user_form,
        "profile_form": profile_form,
        "register_form": register_form
    }

    return render(req, "sign_up.html", data)
    # return HttpResponse("<h1>Sing Up</h1>")


def sign_in(req):
    user = None
    context = {}
    return render(req, "sign_in.html")
    # return HttpResponse("<h1>Sing In</h1>")


def authorize(req):
    user = None
    context = {}
    if req.method == "POST":
        username = req.POST.get('username', )
        password = req.POST.get('password', )
        user = auth.authenticate(username=username, password=password)
    if user is not None:
        print("user found")
        auth.login(req, user)
        return HttpResponseRedirect('/')
    else:
        print("user not found")
        login_error = "User not exist"
        context = {"login_error": login_error}
        return render(req, "sign_in.html")


def logout_func(req):
    if req.user.is_authenticated:
        logout(req)
    return HttpResponseRedirect('/user/')


def student_details_view(req, student_id):
    student = User.objects.get(pk=student_id)
    enrolled_subject_list = Subject.objects.filter(users__pk=student_id)

    context = {
        "student": student,
        "enrolled_subject_list": enrolled_subject_list
    }

    return render(req, 'student-details.html', context)
