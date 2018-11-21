from django.shortcuts import render
from subject.views import get_subject_list


def index(req):
    subject_list = get_subject_list(5)
    print(subject_list)
    context = {"subject_list": subject_list}
    return render(req, 'index.html', context)
