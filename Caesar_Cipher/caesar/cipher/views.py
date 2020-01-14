from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import math
from .forms1 import contactform1
def index(request):
        return HttpResponse("Hello, world.You're at the world of Cipher ")
def contact(request):

        translated = ""
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
        if request.method == 'POST':
                        form= ContactForm(request.POST)
                

                        if form.is_valid():

                                
                                encryption = form.cleaned_data['encryption_type']
                                key = form.cleaned_data['key']
                                sting = form.cleaned_data['string']
                                mode = form.cleaned_data['mode']
                          

                                if encryption == "transposition":
                                      
                                        if mode =='enc':
                                                
                                                
                                                #pyperclip.copy(ciphertext)
                                                ciphertext = ['']*key	
                                                print(ciphertext)
                                                
                                                for column in range(key):  # 0 to 7
                                                        currentIndex = column
                                                        
                                                        while currentIndex < len(sting):
                                                                ciphertext[column] += sting[currentIndex]
                                                                
                                                                currentIndex += key
                                                                
                                                translated =''.join(ciphertext)
                                                

                                        elif mode =='dec':
                                        
                                                numOfColumns = int(math.ceil(len(sting)/float(key)))	
                                                print("numcol>>>",numOfColumns)
                                                numOfRows = key
                                                print(">>>>>> key ",numOfRows)
                                                
                                                numOfShadedBox = (numOfColumns * numOfRows) - len(sting)
                                                
                                                plaintext = [''] * int(numOfColumns)
                                                
                                                column = 0
                                                row = 0
                                                
                                                for symbol in sting:
                                                        plaintext[column] += symbol
                                                        column += 1
                                                
                                                
                                                        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBox):
                                                                column = 0
                                                                row += 1
                                                                
                                                translated = ''.join(plaintext)
                                                
                                        	       		             
                                                        




                                elif encryption == "caesar":
                # if request.method == 'POST':
                #         form= ContactForm(request.POST)
                

                #         if form.is_valid():

                                
                #                 encryption = form.cleaned_data['encryption_type']
                #                 key = form.cleaned_data['key']
                #                 sting = form.cleaned_data['string']
                #                 mode = form.cleaned_data['mode']

                                        for symbol in sting:
                                                if symbol in SYMBOLS:
                                                        symbolindex = SYMBOLS.find(symbol)

                                                        if mode  == "enc":
                                                                translateIndex = symbolindex + key
                                                        elif mode == "dec":
                                                                translateIndex = symbolindex - key

                                                        if translateIndex >= len(SYMBOLS):
                                                                translateIndex = translateIndex - len(SYMBOLS)
                                                        
                                                        elif translateIndex < 0:
                                                                translateIndex = translateIndex + len(SYMBOLS)


                                                        translated = translated + SYMBOLS[translateIndex]
                                                      
                                                else:
                                                        translated  = translated + symbol

                                                


        form = ContactForm()
        return render(request,'form.html',{'form' : form,'translated':translated})    




def form1View(request):
       
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

        return render(request,'form1.html',{'fo':fo})
