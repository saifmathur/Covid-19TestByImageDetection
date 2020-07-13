from django.shortcuts import render
from pymongo import MongoClient
from gridfs import GridFS
from django.core.files.storage import FileSystemStorage

CLIENT = MongoClient('localhost',27017)
DATABASE = CLIENT['CovidProject']
COLLECTION = DATABASE['userData']


# Create your views here.
def index(request):
    return render(request,'covidIndex.html')

def predict(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        image = request.FILES['img']
        imageFile = FileSystemStorage()
        imageFile.save(image.name, image)
        fs = GridFS(DATABASE)
        fs.put(image)
        
        print(image)
        print(request)
    return render(request,'covidIndex.html')


