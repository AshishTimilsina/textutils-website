from django.http import HttpResponse
from django.shortcuts import render

# Index function runs in frontend
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

# Analyze function runs in backend
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    # off means clicking in remove punctuations
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspace = request.POST.get('extraspace','off')
    charcount = request.POST.get('charcount','off')

    #Check which checkbox is on
    # logic  for removing punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # logic  for making text UPPERCASE
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Making text uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # logic for removing newlines
    elif newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params = {'purpose': 'Removing lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # logic for removing extra space
    elif extraspace=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]== " " and djtext[index+1]== " ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': 'Removing Extra space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # logic for counting character of text
    elif charcount=="on":
        analyzed=""
        count=0
        for index,char in enumerate(djtext):
            if djtext[index]== " ":
                pass
            elif ascii(char):
                count=count+1

        params = {'purpose': 'Removing Extra space', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

