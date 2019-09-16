from django.contrib import admin
from django.urls import path
from resumeapp import test
from resumeapp import auth
urlpatterns = [
    path('showtemps/',test.showTemplates.as_view(),name='show_templates'),
    path('selected/<str:id>/',test.processSelectedTemplate.as_view(),name='template_submit'),
    path('enterDetails/',test.enter_details.as_view(),name = 'enter_details'),
    path('getResume/',test.get_resume.as_view(),name = 'get_resume'),
    path('login/',auth.Login.as_view(),name='login'),
    path('logout/',auth.logout_user,name='logout'),
    path('register/',auth.SignUp.as_view(),name='register'),
]