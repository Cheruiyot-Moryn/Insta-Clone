from .models import ImageField
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    profile = Profile.objects.all()
    posts = ImageField.objects.all()

    return render(request,'home.html',{"profile":profile, "posts":posts})
