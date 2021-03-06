"""onlineMath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls', namespace='users')),
    url(r'^exercise/',include('exercise.urls')),
    url(r'^subject/',include('subject.urls',namespace='subject'), ),
    url(r'^calculus_1/',include('calculus1.urls',namespace='calculus1'), ),
    url(r'^simple_math/', include('simpleMath.urls', namespace='simple_math'), ),
]  +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
