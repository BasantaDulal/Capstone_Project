from django.shortcuts import render


def fertilizer_requirement(request):
    return render(request, 'fertilizer_requirement.html')
