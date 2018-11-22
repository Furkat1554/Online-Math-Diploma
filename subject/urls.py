from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_subject_list_view, name='show_subject_list_view'),
    url(r'^subject-details/([\w|\W|\d|\D]+)/$',
        views.show_subject_details,
        name='show_subject_details'),
    url(r'^stream/enroll_user/$',
        views.enroll_user,
        name='enroll_current_user'),
    url(r'^getTopicsList/([\w|\W|\d|\D]+)$',
        views.get_topics_list,
        name='api_get_topic_list'),
    url(r'^solve-topic/([\w|\W|\d|\D]+)/([\w|\W|\d|\D]+)$',
        views.solve_topic,
        name='solve_topic'),

    # streams
    url(r'^streams-view$',
        views.show_stream_list_view,
        name='show_streams_list_view'),

    url(r'^stream/([\w|\W|\d|\D]+)/details$',
        views.get_streams_details,
        name="api_get_streams_details"),

    url(r'^stream/([\w|\W|\d|\D]+)/is-enrolled$',
        views.is_enrolled,
        name="api_get_streams_details"),

    url(r'^streams/([\w|\W|\d|\D]+)$',
        views.show_stream_details,
        name='show_streams_details_view'),

    url(r'^streams$',
        views.get_stream_list,
        name='api_get_streams_list'),

    url(r'^stream-students-enrolled/([\w|\W|\d|\D]+)$',
        views.get_stream_enrolled_students_list,
        name='api_get_stream_students_enrolled_list'),

    url(r'^assignments/$',
        views.get_assignments,
        name='api_get_all_assignments'),
    url(r'^solve-exercise/([\w|\W|\d|\D]+)/([\w|\W|\d|\D]+)$',
        views.get_assignments,
        name='api_get_all_assignments'),

]
