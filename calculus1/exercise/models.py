from django.db import models
from random import *
# Create your models here.

# class HomeWork(models.Model):
#     groupId = models.

class GeneralTools():
    def list_to_int(self,var):
        if not isinstance(var, list):
            return var
        out = []
        for i in var:
            out.append(int(i))
        return out

class Exercise(models.Model):
    def solve(self):
        pass
    def get_expected_answer(self):
        pass
    def generate_example(self):
        pass
    def check_answer(self):
        pass

class GCD(Exercise):
    def solve(self,a, b):
        """Calculate the Greatest Common Divisor of a and b.
        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a

    def get_expected_answer(self,variables):
        return self.solve(variables[0],variables[1])

    def generate_example(self):
        n1 = randint(1,1000)
        n2 = randint(1,1000)
        return [n1,n2]

    def check_answer(self,variables,student_answer):
        variables = GeneralTools().list_to_int(variables)
        expected_answer = self.get_expected_answer(variables)
        if expected_answer == int(student_answer):
            return True
        return False
