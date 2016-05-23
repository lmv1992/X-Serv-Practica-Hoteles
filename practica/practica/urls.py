"""practica URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(.*)/xml$',"hoteles.views.usuario_xml"),
    url(r'^$', "hoteles.views.principal"),
    url(r'^about$', "hoteles.views.about"),
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^alojamientos/admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/profile/$', 'hoteles.views.perfiles'),
    url(r'^alojamientos/accounts/profile/$', 'hoteles.views.perfiles'),
    url(r'^alojamientos$',"hoteles.views.alojamientos"),
    url(r'^alojamientos/(\d+)$',"hoteles.views.alojamientos_id"),
    url(r'^alojamientos/frances',"hoteles.views.nana"),
    url(r'^alojamientos/ingles',"hoteles.views.nana"),	
    url(r'^alojamientos/alojamiento/accounts/profile/$', 'hoteles.views.perfiles'),
    url(r'^(.*)$',"hoteles.views.usuario"),

]
