"""college_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from college import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('apply/',views.apply,name='apply'),
    path('login/',views.login,name='login'),
    path('loginsuccess/',views.appl_form,name='loginsuccess'),
    path('applyfirst/',views.applyfirst,name='applyfirst'),
    path('appl_form/',views.appl_form, name='appl_form'),
    path('login_page/',views.login_page, name='login_page'),
    path('details/',views.details, name='details'),
    path('logout/',views.logout,name='logout'),
    path('details_view/', views.details_view, name='details_view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('board/',views.board,name='board'),
    path('application_form/',views.application_form,name='application_form'),
    path('hall_ticket/',views.hall_ticket,name='hall_ticket')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)