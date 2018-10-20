from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sample$', views.sample, name='sample'),
    url(r'^generate-expression/([\w|\W|\d|\D]+)$',
        views.generate_example,
        name='generate_expression'),
    url(r'^solve-expression$',
        views.solve_expression,
        name='solve_expression')
]
