from django.shortcuts import render
from pymongo import MongoClient
from gridfs import GridFS

from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img
from PIL import Image


model = load_model('covidPredictionModel\covid19_model.h5')


from django.core.files.storage import FileSystemStorage

CLIENT = MongoClient('localhost',27017)
DATABASE = CLIENT['CovidProject']
COLLECTION = DATABASE['userData']


def ImageManagement(imageObj):
    var = Image.open(imageObj,"r")
    var = var.resize((224,224))
    #var.show()
    return var

# Create your views here.
def index(request):
    return render(request,'covidIndex.html')

def predict(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        image = request.FILES['img']
        imageFile = FileSystemStorage()
        imgObj = imageFile.save(image.name, image)
        
        result = ImageManagement(imgObj)
        pred = model.predict(result)
        print(pred)
        

        
        fs = GridFS(DATABASE)
        image_id = fs.put(image) #for finding and keeping track
        dataDict = {
            "name":name,
            "age":age,
            "filename":image.name,
            "file_id": image_id
        }
        dataInsertion = COLLECTION.insert_one(dataDict)
        #print(pred)
    return render(request,'covidIndex.html')


