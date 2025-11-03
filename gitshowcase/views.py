from django.shortcuts import render

def home(request):
    context = {'user': request.user}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')