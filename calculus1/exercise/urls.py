from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='gcd_index'),
    url(r'^gcd_create_assignment/$', views.create_assignment, name='gcd_create_assignment'),
    url(r'^gcd_solve_assignment/$', views.solve, name='gcd_solve'),
    url(r'^gcd_check_answer/$', views.check_answer, name='gcd_check_answer'),
    url(r'^gcd_give_assignment/$', views.give_assignment, name='gcd_give_assignment'),
]
