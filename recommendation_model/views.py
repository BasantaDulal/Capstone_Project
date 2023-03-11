from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')


def crop_recommend(request):
    if request.method == 'POST':
        n = request.POST['n']
        p = request.POST['p']
        k = request.POST['k']
        temp = request.POST['temp']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        rainfall = request.POST['rainfall']
        y_pred = model.predict([[n, p, k, temp, humidity, ph, rainfall]])
        return render(request,'crop_recommend.html', {'result': y_pred})
    return render(request, 'crop_recommend.html')
