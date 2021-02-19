from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django import forms
import json
from decimal import *
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


def home(request):
    return render(request,'home.html',{"addnewcontactlink":"http://127.0.0.1:8000/addnewcontact",
                                       "getallcontactslink":"http://127.0.0.1:8000/getallcontacts",
                                       "searchcontactlink":"http://127.0.0.1:8000/searchcontact",
                                       "deletecontactlink":"http://127.0.0.1:8000/deletecontact"}
                )


def addnewcontact(request):
    
    nametoenter=request.POST.get('Fullname')
    phonenumbertoenter=request.POST.get('phno')
    emailtoenter=request.POST.get('emailadd')
    if(nametoenter!=None and emailtoenter!=None ):
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO phonebook.`contact-list` (name, phone, email)
                    VALUES ('{}', '{}', '{}')""".format(nametoenter, phonenumbertoenter, emailtoenter))
    
    return render(request, 'addnewcontact.html',{"key1":"value1"})


def getallcontacts(request):
    cursor = connection.cursor()
    cursor.execute("""SELECT name, phone, email from phonebook.`contact-list` ORDER BY name;""")
    result=cursor.fetchall()
    list1=[]
    c=1
    empty=True

    for i in result:
        list1.append(str(c)+". "+str(i[0]))
        list1.append(i[1])
        list1.append(i[2])
        list1.append(" ")
        c+=1
    print(list1)

    return render(request, 'getallcontacts.html',{"getallcontacts":list1,"Total":len(list1)//4})


def searchcontact(request):
    nametoenter=request.POST.get('Fullname')
    
    emailtoenter=request.POST.get('emailadd')

    cursor = connection.cursor()
    cursor.execute("""SELECT name, phone, email FROM phonebook.`contact-list` WHERE name LIKE '%{}%' and email LIKE '%{}%' ;""".format(nametoenter, emailtoenter))
    result=cursor.fetchall()
    list1=[]
    c=0
  
    for i in result:
        c = c + 1
        list1.append(str(c)+". "+str(i[0]))
        list1.append(i[1])
        list1.append(i[2])
        list1.append(" ")



    return render(request, 'searchcontacts.html',{"searchcontacts":list1,"Total":len(list1)//4})


def deletecontact(request):
    nametoenter=request.POST.get('Fullname')
    
    emailtoenter=request.POST.get('emailadd')

    cursor = connection.cursor()
    cursor.execute("""SELECT name, phone, email FROM phonebook.`contact-list` WHERE name LIKE '%{}%' and email LIKE '%{}%' ;""".format(nametoenter, emailtoenter))
    result=cursor.fetchall()
    list1=[]
    c=0
  
    for i in result:
        c = c + 1
        list1.append(str(c)+". "+str(i[0]))
        list1.append(i[1])
        list1.append(i[2])
        list1.append(" ")
    

    cursor = connection.cursor()
    cursor.execute("""DELETE FROM phonebook.`contact-list` WHERE name='{}' and email='{}';""".format(nametoenter, emailtoenter))
    print(cursor.fetchall())

    return render(request, 'deletecontact.html',{"searchcontacts":list1,"Total":len(list1)//4})
  
    

