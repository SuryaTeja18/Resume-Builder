from django.contrib import admin
from django.urls import path
from resumeapp import test
urlpatterns = [
    path('test/',test.demo.as_view(),name='template1'),
    path('test/submit',test.demo_submit.as_view(),name='template_submit'),

]