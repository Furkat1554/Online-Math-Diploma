from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_topic_list, name='show_topic_list'),
    url(r'^show-exercise/([0-9]+)/$',
        views.show_exercise,
        name='show_exercise'),
    url(r'^get-generated-exercise/([0-9]+)/$',
        views.get_exercise,
        name='get_generate_exercise'),
    url(r'^check-solution/$',
        views.check_solution,
        name='check_solution'),
]
