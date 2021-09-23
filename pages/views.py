from django.shortcuts import render

# Create your views here.

#Bu yerda saytlarni kurinishlarini yaratsak buladi

from django.http import HttpResponse

def home_view(request,*args,**kwargs):
    # return HttpResponse("<h1>Home pagedasiz</h1>")

    #templates papka ochib uni ichiga uzimizni html faylarimizni yozamiz
    return render(request, "home.html", {})

def contact(request,*args,**kwargs):
    # return HttpResponse("<h1>Contact bulimidasiz</h1>")
    about_me={
        'number':997707375,
        'Name':'davron',
        'bu true':True,
        'html_code':'<h3>html uchun |safe </h3>',
        'lists':[
            111,222,333,'Abc',1
        ]
    }
    return render(request,"contact.html",about_me)