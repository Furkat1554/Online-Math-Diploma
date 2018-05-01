# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import Topic, Assignment, AssignmentTopic
import random
import math
# Create your views here.

def get_topic_list(limit = 0):
    topic = Topic.objects.all()
    return topic if limit == 0 else topic[:limit]

def show_topic_list(req):
    topic = get_topic_list()
    context = {
        "topic_list": topic
    }
    return render(req,'topic-list.html',context)

def show_exercise(req,topic_id):
    topic = Topic.objects.get(pk=topic_id)
    context = {
        "topic": topic
    }
    return render(req,'exercise.html',context)

def get_exercise(req,topic_id):
    topic = Topic.objects.get(pk=topic_id)
    exercise = generate_exercise(topic.function_name)
    context = {
        'expression' : exercise
    }
    return JsonResponse(context)

@csrf_exempt
def check_solution(req):
    answers = [req.POST.get("answers[]")[0],req.POST.get("answers[]")[0]]
    expression = req.POST.get("expression")
    topic_id = req.POST.get("topicId")
    print("ONE: ",topic_id, expression,answers)

    topic = Topic.objects.get(pk=topic_id)
    result = solve_exerice(topic.function_name,expression,answers)
    print("Result: ",result)

    context = {
        "result": result
    }
    return JsonResponse(context);
def generate_exercise(name):
    if name == 'ch_0_0_simple_qe':
        return generate_ch_0_0_simple_qe()

def solve_exerice(name,expression,answers):
    expected = []
    if(name == 'ch_0_0_simple_qe'):
         expected = solve_ch_0_0_simple_qe(expression)

    if len(expected) != len(expression):
        return False

    trueCount = 0
    for i in range(0,len(answers)):
        foundFlag = False
        for j in range(0,len(expected)):
            if answers[i] == expected[j]:
                foundFlag = True
                expected.splice(j,1)
                trueCount += 1
                break
        if not foundFlag:
            return False
        if expected.length == 0:
            break

        return True if answers.length == trueCount else False

def generate_ch_0_0_simple_qe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    out = ""
    if random.randint(0,2) == 0:
        out += "-"
    out += str(a)+"x^2"

    out += "-" if random.randint(0,2) == 1 else "+"
    out += str(b)+"x"

    out += "-"if  random.randint(0,2) == 0 else "+"
    out += str(c)+"=0"

    return out

def solve_ch_0_0_simple_qe(expression):
    result = []
    a,b,c = parse_ch_0_0_simple_qe(expression)
    result.append(( (-1)*b - math.sqrt(math.pow(float(b),2) - float(4*a*c)) ) / (2 * a))
    result.append(( (-1)*b + math.sqrt(math.pow(float(b),2) - float(4*a*c)) ) / (2 * a))
    return result

def parse_ch_0_0_simple_qe(expression):
    a = int(expression[0:expression.find("x^")])
    expression = expression.replace(expression[0:expression.find("x^")+3],"")
    b = int(expression[0:expression.find("x")])
    expression = expression.replace(expression[0:expression.find("x")+1],"")
    c = int(expression[:expression.find("=")])

    return [a,b,c]
