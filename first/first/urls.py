"""first URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/',include('django.contrib.auth.urls')),
    url(r'^Student_details',views.Student_details_view),
    url(r'^index',views.Student_form_view),
    url(r'^$',views.Home_view),
    url(r'^signup',views.StudentSignup_view),
    url(r'^python',views.pythonexam_view),
    url(r'^java',views.javaexam_view),
    url(r'^aptitude',views.aptitudeexam_view),
    url(r'^insert',views.StudentInsert_view),
    url(r'^delete/(?P<id>\d+)/$',views.StudentDelete_view),
    url(r'^update/(?P<id>\d+)/$',views.StudentUpdate_view),
]
