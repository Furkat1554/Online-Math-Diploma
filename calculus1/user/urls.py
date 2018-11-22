from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^create_user/$', views.register_user, name='create_user'),
    url(r'^$', views.profile, name='profile'),
    url(r'^authorize/$', views.authorize, name='authorize'),
    url(r'^logout/$', views.logout_func, name='logout_view'),
    url(r'^student-details/([0-9]+)/$', views.student_details_view, name='student_details_view'),
]
