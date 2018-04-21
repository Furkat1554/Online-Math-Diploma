from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Subject
from user.models import Profile

def get_all_subject_list(limit = 0):
    return Subject.objects.all() if limit == 0 else Subject.objects.all()[:limit]

def get_enrolled_student_list(subject_id):
    users = User.objects.filter(subject__pk=subject_id)
    return users;

def get_enrolled_subject_list(student_id):
    subject_list = Subject.objects.filter(users__id=student_id)
    return subject_list

def enroll_student(student_id,subject_id):
    user = User.objects.get( pk = student_id )
    subject = Subject.objects.get( pk = subject_id)
    subject.users.add(user)
    pass

def unenroll_student(student_id,subject_id):
    user = User.objects.get( pk = student_id )
    subject = Subject.objects.get( pk = subject_id)
    subject.users.remove(user)

def get_by_student_and_subject(student_id,subject_id):
    # subject = Subject.objects.get(pk=subject_id).filter(user__id=student_id)
    subject = Subject.objects.filter(id=subject_id,users__id=student_id)
    print("id enroll: " + str(subject_id) + " " + str(student_id))
    print(subject)
    return subject

# Create your views here.
#
@login_required(login_url='/user')
def show_subject_list_view(req):
    subject_list = get_all_subject_list()
    context = {"subject_list":subject_list}
    return render(req,'subject-list.html',context)

@login_required(login_url='/user')
def show_subject_details(req,subject_id):
    subject = Subject.objects.get(pk=subject_id)
    student_list = get_enrolled_student_list(subject_id)
    is_current_user_enrolled = get_by_student_and_subject(req.user.id,subject_id)
    context = {
    "subject": subject,
    "enrolled_students": student_list,
    "is_current_user_enrolled": is_current_user_enrolled}
    return render(req,'subject-details.html',context)

def enroll_current_user(req):
    subject_id = req.POST.get("subject_id")
    enroll_key = req.POST.get('enroll_key')

    subject = Subject.objects.get(pk=subject_id)
    if(subject.enroll_key == enroll_key):
        subject.users.add(req.user)

    return redirect("/subject/subject-details/"+subject_id)

def unenroll_current_user(req):
    subject_id = req.POST.get("subject_id")

    subject = Subject.objects.get(pk=subject_id)

    subject.users.remove(req.user)

    return redirect("/subject/subject-details/"+subject_id)
