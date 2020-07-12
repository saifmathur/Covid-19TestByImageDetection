from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'covidIndex.html')

def predict(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.POST.get('img')
        print(request)
        return render(request,'covidIndex.html')