from django.shortcuts import render


def irrigation_planning(request):
    return render(request, 'irrigation_planning.html')
