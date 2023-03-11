from django.shortcuts import render


def crop_yield_prediction(request):
    return render(request, 'crop_yield_prediction.html')
