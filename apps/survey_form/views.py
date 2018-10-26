from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, "survey_form/index.html")

def result(request):
    return render(request, "survey_form/result.html")

def process(request):
    if "count" in request.session:
        request.session['count'] == request.session['count']
    else:
        request.session['count'] = 0
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['dojo'] = request.POST['dojo']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['count'] = int(request.session['count']+1)
        return redirect("/result")
    else:
        return redirect(request, "/")
