from django.shortcuts import render
from .models import Widget

# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    return render(request, 'home.html',{widget_list:widget_list})