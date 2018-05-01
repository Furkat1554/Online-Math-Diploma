from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Subject
from user.models import Profile

def get_subject_list(limit = 0):
    return Subject.objects.all() if limit == 0 else Subject.objects.all()[:limit]

def get_stream_list(limit = 0):
    return Stream.objects.all() if limit == 0 else Stream.objects.all()[:limit]


def get_enrolled_student_list(subject_id):
    users = User.objects.filter(stream__pk=stream_id)
    return users;

def get_enrolled_stream_list(student_id):
    subject_list = Stream.objects.filter(users__id=student_id)
    return subject_list

def enroll_student(student_id,subject_id):
    user = User.objects.get( pk = student_id )
    stream = Stream.objects.get( pk = stream_id)
    stream.users.add(user)
    pass

def unenroll_student(student_id,stream_id):
    user = User.objects.get( pk = student_id )
    stream = Stream.objects.get( pk = stream_id)
    stream.users.remove(user)

def get_by_student_and_stream(student_id,stream_id):
    # subject = Subject.objects.get(pk=subject_id).filter(user__id=student_id)
    stream = Stream.objects.filter(id=stream_id,users__id=student_id)
    print("id enroll: " + str(stream_id) + " " + str(student_id))
    print(stream)
    return stream

# Create your views here.
#
@login_required(login_url='/user')
def show_subject_list_view(req):
    subject_list = get_subject_list()
    context = {"subject_list":subject_list}
    return render(req,'subject-list.html',context)

@login_required(login_url='/user')
def show_subject_details(req,subject_id):
    subject = Subject.objects.get(pk=subject_id)
    context = {
    "subject": subject,}
    return render(req,'subject-details.html',context)

def enroll_current_user(req):
    stream_id = req.POST.get("stream_id")
    enroll_key = req.POST.get('enroll_key')

    stream = Stream.objects.get(pk=stream_id)
    if(stream.enroll_key == enroll_key):
        stream.users.add(req.user)

    return redirect("/subject/subject-details/"+stream_id)

def unenroll_current_user(req):
    subject_id = req.POST.get("stream_id")

    stream = Stream.objects.get(pk=stream_id)

    stream.users.remove(req.user)

    return redirect("/subject/subject-details/"+stream_id)

@login_required(login_url='/user')
def show_stream_list_view(req,res):
    subject_list = get_subject_list()
    context = {"subject_list":subject_list}
    return render(req,'subject-list.html',context)

@login_required(login_url='/user')
def show_stream_details(req,subject_id):
    stream = Stream.objects.get(pk=stream_id)
    student_list = get_enrolled_student_list(stream_id)
    is_current_user_enrolled = get_by_student_and_stream(req.user.id,stream_id)
    context = {
    "stream": stream,
    "enrolled_students": student_list,
    "is_current_user_enrolled": is_current_user_enrolled}
    return render(req,'subject-details.html',context)
