from django.shortcuts import render


def home_view(request):
    context = {}
    return render(request, 'core/home.html', context)
