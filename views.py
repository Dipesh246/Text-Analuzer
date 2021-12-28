# I made this file - ROHIT
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')
    


def analyze(request):
    djtext=request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    if removepunc=="on":
        panctution='''≈&'⁂@\[]}{•‸⎀^:🄯,(ɔ)©¤†‡°*⌀÷⸗…=!ª❧.,♀♂⚥>,«»,☞,·,‽,',¡,¿,<,◊,☞,º,#,№,(),%,‰,.,⌑,+,?,",',®,§,;,℠,/,℗,⌑,∴,⁀,~,™,_,|,|,/'''
        analyzed = ""
        for char in djtext:
            if char not in panctution:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r": 
                analyzed = analyzed + char
        params = {'purpose':'Removed New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if spaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
        
    #if charcounter=="on":
        #analyzed = "total character : "+ str(len(djtext))
        #params = {'purpose':'Counted Number of Character', 'analyzed_text': analyzed}

    
        


    return render(request, 'analyze.html', params)
        
        

def capitalize(request):
    djtext=request.GET.get('text', 'default')
    fullcaps = request.GET.get('fullcaps', 'off')
    
    

def newlineremover(request):
    return HttpResponse('''<h1>New Line Remover</h1> <a href="/">Back</a>''')

def spaceremover(request):
    return HttpResponse('''<h1>Space Remover</h1> <a href="/">Back</a>''')


def charcounter(request):
    return HttpResponse('''<h1>Charecter Counter</h1> <a href="/">Back</a>''')
