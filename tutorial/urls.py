"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
#from snippets import views
from tutorial import views
#from django.conf.urls import patterns
urlpatterns =[
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    #url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^sign_up/$', views.SignUp.as_view(), name="sign_up"),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))

]
