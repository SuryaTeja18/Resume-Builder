from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import resolve
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import *
from django.db.models import Count,Sum
import json
import boto3
from django import forms
import docx

class details(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter Name','name':'name'}))
    skills = forms.CharField(widget=forms.TextInput(attrs={'class':'input','placeholder':'Enter skills','name':'skills'}))


dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAQAEZBTOIKBXNZBK5', aws_secret_access_key='PqV7P/0cetfpYy5Pj6c7fYE7lC6JTiYGpL2m80XH', region_name='us-east-1')
s3 = boto3.resource('s3',aws_access_key_id='AKIAQAEZBTOIKBXNZBK5', aws_secret_access_key='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', region_name='us-east-1')
'''ec2 = boto3.client('ec2',aws_access_key_id='AKIAQAEZBTOIKBXNZBK5', aws_secret_access_key='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', region_name='us-east-1')'''

class demo(View):
    def get(self, request, *args, **kwargs):
        return render(request, "showtemplates.html",{'demo':request})

class demo_submit(View):
    def get(self,request,*args,**kwargs):
        if(True):
            # table = dynamodb.Table('demo')
            # print(table)
            #client = boto3.client('s3',aws_access_key_id='AKIAQAEZBTOIKBXNZBK5', aws_secret_access_key='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', region_name='us-east-1')
            #response = client.list_objects(Bucket='18suryateja.demo1')
            # for content in response['Contents']:
            #     obj_dict = client.get_object(Bucket='18suryateja.demo1', Key=content['Key'])
            #     print(content['Key'], obj_dict['LastModified'])
            #return HttpResponse(response['Key'])
            #table = dynamodb.Table('demo')
            #response = table.put_item(Item={'house':'white','name':'whstu'})
            path1 = "./template1.png"
            path2 = "./template2.png"
            s3.Bucket('18suryateja.demo1').upload_file(path1,Key='resumeTemplate1.png')
            s3.Bucket('18suryateja.demo1').upload_file(path2,Key='resumeTemplate2.png')
            return HttpResponse("21212")

class enter_details(View):
    def get(self,request,*args,**kwargs):
        return render(request,"details.html")
    def post(self,request,*args,**kwargs):
        print('post methodddd')
        return HttpResponse(kwargs['id'])

class get_resume(View):
    def post(self,request,*args,**kwargs):
        print('post methodddd')
        return HttpResponse(kwargs['id'])


class showTemplates(View):
    def get(self,request,*args,**kwargs):
        return render(request,"showtemplates.html")

class processSelectedTemplate(View):
    def get(self,request,*args,**kwargs):
        return render(request,'details.html',{'id':kwargs['id']})
    def post(self,request,*args,**kwargs):
        data = request.POST
        doc = docx.Document()
        doc.add_heading(data['user_name'], 0)
        doc.add_heading(data['email'],4)
        doc.add_heading(data['phone'],4)
        doc.add_heading('Skills', 2)
        doc_para = doc.add_paragraph(' ')
        for skill in data['skills'].split(','):
            doc_para.add_run(skill+', ').bold = True
        # add a page break to start a new page
        #doc.add_page_break()
        # add a heading of level 2
        doc.add_heading('Education', 2)
        doc_para = doc.add_paragraph(' ')
        for ed in data['edu'].split(','):
            doc_para.add_run(ed+', ').bold = True
        # pictures can also be added to our word document
        # width is optional
        #    doc.add_picture('path_to_picture')
        # now save the document to a location
        doc.add_heading('Awards', 2)
        doc_para = doc.add_paragraph(' ')
        for award in data['awards'].split(','):
            doc_para.add_run(award+', ').bold = True
        doc.save(data['name']+'.docx')
        res = s3.Bucket('18suryateja.demo1').upload_file(data['name']+'.docx', Key=data['name']+'.docx')
        table = dynamodb.Table('demo')
        response = table.put_item(Item={'house':'https://s3.ap-south-1.amazonaws.com/18suryateja.demo1/'+data['name'],'name':data['name']})
        bucket_file_path = "https://s3.ap-south-1.amazonaws.com/18suryateja.demo1/"+data['name']+'.docx'
        return HttpResponse(f"<a href={bucket_file_path}><button class='button'>Download</button></a>")