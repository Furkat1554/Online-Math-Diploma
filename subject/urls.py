from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_subject_list_view, name='show_subject_list_view'),
    url(r'^subject-details/([\w|\W|\d|\D]+)/$',
        views.show_subject_details,
        name='show_subject_details'),
    url(r'^enroll_user/$',
        views.enroll_current_user,
        name='enroll_current_user'),
    url(r'^unenroll_user/$',
        views.unenroll_current_user,
        name='unenroll_current_user'),
    url(r'^getTopicsList/([\w|\W|\d|\D]+)$',
        views.get_topics_list,
        name='api_get_topic_list'),
    url(r'^solve-topic/([\w|\W|\d|\D]+)/([\w|\W|\d|\D]+)$',
        views.solve_topic,
        name='solve_topic'),
]
