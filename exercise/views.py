from django.shortcuts import render
from exercise.models import GCD
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(req):
    return render(req,'gcd/gcd_index.html')

def solve(req):
    gcd = GCD()
    variables = gcd.generate_example()
    data = {
        'variables' : variables,
    }
    return render(req,'gcd/gcd_solve_example.html', data)

def create_assignment(req):
    return render(req,'gcd/gcd_create_assignment.html')

@csrf_exempt
def check_answer(req):
    gcd = GCD()
    answer = int(req.POST.get("answer"))
    variables = req.POST.getlist("variables[]")
    return JsonResponse({"result": gcd.check_answer(variables,answer)})

def give_assignment(req):
    return HttpResponseRedirect("/exercise/")
