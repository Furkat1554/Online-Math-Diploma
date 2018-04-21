from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_subject_list_view, name='show_subject_list_view'),
    url(r'^subject-details/([0-9]+)/$',
        views.show_subject_details,
        name='show_subject_details'),
    url(r'^enroll_user/$',
        views.enroll_current_user,
        name='enroll_current_user'),
    url(r'^unenroll_user/$',
        views.unenroll_current_user,
        name='unenroll_current_user'),
]
