from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Subject, Stream, Topic, Assignment, AssignmentTopic, AssignmentDone
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def get_subject_list(limit=0):
    return Subject.objects.all() if limit == 0 else Subject.objects.all()[:limit]


def get_subject_by_code(subject_code):
    if None == subject_code:
        return ""

    return Subject.objects.get(subject_code=subject_code)


def get_stream_list_all(limit=0):
    return Stream.objects.all() if limit == 0 else Stream.objects.all()[:limit]


def get_enrolled_student_list(subject_id):
    users = User.objects.filter(stream__pk=stream_id)
    return users;


def get_enrolled_stream_list(student_id):
    subject_list = Stream.objects.filter(users__id=student_id)
    return subject_list


@csrf_exempt
def enroll_student(student_id, subject_id):
    user = User.objects.get(pk=student_id)
    stream = Stream.objects.get(pk=stream_id)
    stream.users.add(user)
    pass


def unenroll_student(student_id, stream_id):
    user = User.objects.get(pk=student_id)
    stream = Stream.objects.get(pk=stream_id)
    stream.users.remove(user)


def get_by_student_and_stream(student_id, stream_id):
    # subject = Subject.objects.get(pk=subject_id).filter(user__id=student_id)
    stream = Stream.objects.filter(id=stream_id, users__id=student_id)
    print("id enroll: " + str(stream_id) + " " + str(student_id))
    print(stream)
    return stream


@csrf_exempt
def show_subject_list_view(req):
    subject_list = get_subject_list()
    context = {"subject_list": subject_list}
    return render(req, 'subject-list.html', context)


# @login_required(login_url='/user')
@csrf_exempt
def show_subject_details(req, subject_id):
    subject = Subject.objects.get(subject_code=subject_id)
    context = {
        "subject": subject, }
    return render(req, 'subject-details.html', context)


@csrf_exempt
def enroll_user(req):
    if 'GET' == req.method:
        return
    user_id = req.POST.get("userId")
    enroll_key = req.POST.get('enrollKey')
    stream_code = req.POST.get('streamCode')
    enroll_operation = make_boolean(req.POST.get('enrollOperation'))

    if stream_code is None:
        return JsonResponse({
            'status': 422,
            'errorMessage': 'No stream code is provided'
        })

    if user_id is None or (user_id.isdigit() and int(user_id) == 0):
        user = req.user
    elif user_id.isdigit() and int(user_id) == 0:
        user = User.objects.get(pk=int(user_id))
    else:
        return JsonResponse({
            'status': 422,
            'errorMessage': 'invalid user id'
        })

    stream = Stream.objects.get(stream_code=stream_code)

    if enroll_operation and enroll_key is not None \
            and len(enroll_key) > 0 and stream.enroll_key == enroll_key:
        stream.users.add(user)
    elif enroll_operation and enroll_key is not None \
            and len(enroll_key) > 0 and stream.enroll_key != enroll_key:
        return JsonResponse({
            'status': 200,
            'errorMessage': 'Wrong enroll key'
        })
    elif not enroll_operation:
        stream.users.remove(req.user)
    else:
        return JsonResponse({
            'status': 422,
            'errorMessage': 'Uknown operation'
        })

    return JsonResponse({
        'status': 200,
        'result': 'Success'
    })


@csrf_exempt
@login_required(login_url='/user')
def show_stream_list_view(req, ):
    return render(req, 'stream-list.html')


@csrf_exempt
@login_required(login_url='/user')
def get_stream_list(req):
    limit = req.GET.get('limit')
    limit = 0 if limit is None else int(limit)
    stream_list = serializers.serialize('json', get_stream_list_all(limit))
    context = {
        "streamList": stream_list
    }
    return JsonResponse(context)


@csrf_exempt
def streams_post_router(req):
    if req.method.POST == 'POST':
        return is_enrolled(req)
    elif req.method.GET == 'GET':
        return get_stream_list(req)


@csrf_exempt
@login_required(login_url='/user')
def get_stream_enrolled_students_list(req, stream_code):
    pass


@csrf_exempt
@login_required(login_url='/user')
def show_stream_details(req, stream_code):
    return render(req, 'stream-details.html')


@csrf_exempt
def is_enrolled(req, stream_code):
    user_id = req.POST.get('user_id')
    if stream_code is None or stream_code == '':
        context = {
            'errorMessage': 'No stream code is provided'
        }
        return JsonResponse(context)

    if user_id is None or user_id == 0:
        user = req.user
    else:
        user = User.objects.get(pk=user_id)

    stream = Stream.objects.get(stream_code=stream_code)
    if user.is_staff or user.is_superuser or stream.users.filter(pk=user.pk).exists():
        is_user_enrolled = True
    else:
        is_user_enrolled = False

    context = {'isUserEnrolled': is_user_enrolled}
    return JsonResponse(context)


def get_streams_details(req, stream_code):
    stream = Stream.objects.get(stream_code=stream_code)

    current_user = req.user
    is_user_enrolled = stream.users.filter(pk=current_user.pk).exists()

    stream = serializers.serialize('json', [stream])

    context = {
        'error': '421',
        'errorMessage': 'No access, user is not enrolled'
    }

    if is_user_enrolled:
        context = {
            "stream": stream,
            "isCurrentUserEnrolled": is_user_enrolled
        }

    return JsonResponse(context)


# Topic part
def retrieve_topics_list(subject_code="", limit=0):
    if subject_code == "":
        return []
    subject = get_subject_by_code(subject_code)
    return Topic.objects.filter(subject_id=subject.id) if limit == 0 else Topic.objects.get(subject_id=subject.id)[
                                                                          :limit]


def get_topics_list(req, subject_code):
    topic_list = retrieve_topics_list(subject_code, 0)
    tlist = []
    for t in topic_list:
        tlist.append(t)
    topic_list = serializers.serialize('json', tlist)
    context = {
        "topicList": topic_list
    }
    return JsonResponse(context)


def solve_topic(req, subject_code, topic_code):
    return render(req, 'solve-topic.html')
    pass


@csrf_exempt
def get_assignments(req):
    if "POST" == req.method:
        user_id = req.POST.get('userId')
        if user_id is not None and not user_id.isdigit():
            return JsonResponse({
                'status': 422,
                'errorMessage': 'Invalid `userId`. Integers only accepted'
            })
        else:
            user_id = int(user_id)

        if user_id is None or user_id == 0:
            user = req.user
        else:
            user = User.objects.get(pk=user_id)

        stream_code = req.POST.get('streamCode')

        is_exam = req.POST.get('isExam')
        if is_exam is not None:
            is_exam = make_boolean(is_exam)
        else:
            is_exam = False

        if stream_code is not None:
            stream_assignment = get_stream_assignments(user, stream_code, is_exam)
            return JsonResponse(stream_assignment)

        streams_enrolled = Stream.objects.filter(users=user)
        assignments_list = Assignment.objects.filter(stream_id__in=streams_enrolled, is_exam=is_exam)
        assignments = []
        for ass in assignments_list:
            assignment = get_assignment_details(user, ass)
            if assignment is None:
                continue
            assignments.append(assignment)
        result = {
            'status': 200,
            'assignments': assignments,
        }
        return JsonResponse(result)


def get_stream_assignments(user, stream_code, is_exam):
    stream = Stream.objects.get(stream_code=stream_code)
    if not stream.users.filter(pk=user.pk).exists():
        return {
            'status': 403,
            'errorMessage': 'User is not enrolled'
        }
    assignment = Assignment.objects.filter(stream_id=stream, is_exam=is_exam)
    result = {
        'status': 200,
        'assignments': []
    }
    for ass in assignment:
        result['assignments'].append(get_assignment_details(user, ass))

    return result


def get_assignment_details(user, assignment):
    result = {
        'assignmentId': assignment.id,
        'assignmentName': assignment.title,
        'examplesCount': 0,
        'solvedCount': 0,
        'assignments': [],
        'assignmentsDone': [],
    }

    assignment_topics = AssignmentTopic.objects.filter(assignment_id=assignment)
    if assignment_topics.exists():
        for ass_tp in assignment_topics:
            result['examplesCount'] += int(ass_tp.example_amount)
            if ass_tp is not None:
                assignment_dict = {'assignmentId': ass_tp.id,
                                   'exampleAmount': ass_tp.example_amount,
                                   'points': ass_tp.points,
                                   'subjectCode': ass_tp.assignment_id.stream_id.subject_id.subject_code,
                                   'topicCode': ass_tp.topic_id.function_code}
                result['assignments'].append(assignment_dict)

    assignment_done = AssignmentDone.objects.filter(assignment_id=assignment, user_id=user)

    if assignment_done.exists():
        for done in assignment_done:
            if done is not None:
                assignment_done_dict = {'assignmentId': done.assignment_id.id,
                                        'assignmentTopicCode': done.assignment_topic_id.topic_id.function_code,
                                        'exampleAmount': done.count,
                                        'isDone': done.is_done}
                result['assignmentsDone'].append(assignment_done_dict)
            result['solvedCount'] += int(done.count)
    return result


def make_boolean(val):
    return val.upper() == 'TRUE'
