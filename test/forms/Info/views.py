from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactform1

def contact(request):
    # return HttpResponse("<h1>Hi this is Zaka from Views</h1>")

# Create your views here.
    
    if request.method == 'POST':
        
            fo = contactform1(request.POST)
           
            if fo.is_valid():
                    
                    name = fo.cleaned_data['name']
                    email = fo.cleaned_data['email']
                    category = fo.cleaned_data['category']
                    sub = fo.cleaned_data['subject']
                    message = fo.cleaned_data['body']
                    
                    print(name,email,category,sub,message)


  


    fo = contactform1()

    return render(request,'form.html',{'fo':fo})
