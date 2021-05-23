from django.shortcuts import render
from travelapp.models import Place,Team
# Create your views here.
def index(request):
    obj = Place.objects.all()
    tm = Team.objects.all()
    return render(request,'travelapp/home.html',{'obj':obj,'tm':tm})