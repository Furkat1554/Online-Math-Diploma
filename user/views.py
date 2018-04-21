from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from subject.models import Subject

# from ..forms import UserForm
from .forms import *
# Create your views here.

def profile(req):
    return render(req,"profile.html")
    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def create_user(req):
    register_form = UserCreationForm()
    if req.method == "POST":

        new_user_form = UserCreationForm(req.POST)
        if new_user_form.is_valid():
            user = User()
            user.username = req.POST.get('username')
            user.password = new_user_form.cleaned_data['password1']
            user.first_name = req.POST.get('first_name')
            user.last_name = req.POST.get('last_name')
            user.profile.grade = req.POST.get('grade')
            user.email = req.POST.get('email')
            user.save()

            return HttpResponseRedirect('/')
        else:
            register_form = new_user_form
            context = {'register_form': register_form}
            return render(req, 'sign_up.html')

def register_user(req):
    if req.method == 'POST':
        user_form = UserForm(req.POST)
        profile_form = ProfileForm(req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # profile = profile_form.save()
            user.refresh_from_db()
            user.profile.student_grade = profile_form.cleaned_data.get('student_grade')
            user.save();
            # messages.success(req, _('Your profile was successfully updated!'))
            print('successfylly registered')
            return redirect('users:profile')
        else:
            # messages.error(req, _('Please correct the error below.'))
            print('Please correct the error below.')
    else:
        user_form = UserForm(instance=req.user)
        profile_form = ProfileForm(instance=req.user.profile)
        print('not post')
    return render(req, 'index.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def sign_up(req):
    user_form = UserForm()
    profile_form = ProfileForm()
    register_form = RegisterForm()
    data = {
        "user_form" : user_form,
        "profile_form" : profile_form,
        "register_form": register_form
    }

    return render(req,"sign_up.html",data)
    # return HttpResponse("<h1>Sing Up</h1>")

def sign_in(req):
    user = None
    context = {}
    return render(req,"sign_in.html")
    # return HttpResponse("<h1>Sing In</h1>")

def authorize(req):
    user = None
    context = {}
    if req.method == "POST":
        username = req.POST.get('username',)
        password = req.POST.get('password',)
        user = auth.authenticate(username=username, password=password)
    if user is not None :
        print("user found")
        auth.login(req, user)
        return HttpResponseRedirect('/')
    else:
        print("user not found")
        login_error = "User not exist"
        context = {"login_error": login_error}
        return render(req,"sign_in.html")

def logout_func(req):
    if req.user.is_authenticated:
        logout(req)
    return HttpResponseRedirect('/user/')

def student_details_view(req,student_id):
    student = User.objects.get( pk = student_id )
    enrolled_subject_list = Subject.objects.filter( users__pk = student_id )

    context = {
        "student": student,
        "enrolled_subject_list": enrolled_subject_list
    }

    return render(req,'student-details.html',context)
