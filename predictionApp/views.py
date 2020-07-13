from django.shortcuts import render
from pymongo import MongoClient
from gridfs import GridFS

from tensorflow import keras
#model = keras.models.load_model('\covidPrediction\covid19_model.h5')


#from django.core.files.storage import FileSystemStorage

CLIENT = MongoClient('localhost',27017)
DATABASE = CLIENT['CovidProject']
COLLECTION = DATABASE['userData']


# Create your views here.
def index(request):
    return render(request,'covidIndex.html')

def predict(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES['img']
        open(image)
        #imageFile = FileSystemStorage()
        #imageFile.save(image.name, image)
        fs = GridFS(DATABASE)
        image_id = fs.put(image) #for finding and keeping track
        dataDict = {
            "name":name,
            "age":age,
            "filename":image.name,
            "file_id": image_id
        }
        dataInsertion = COLLECTION.insert_one(dataDict)
        #print(image)
        #print(request)
    return render(request,'covidIndex.html')


