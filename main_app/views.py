from django.shortcuts import render,redirect
from .models import Widget
from django.views.generic.edit import DeleteView
from .forms import WidgetForm
from django.db.models import Sum


# Create your views here.
def index(request):
    widget_list = Widget.objects.all()
    widget_form = WidgetForm()
    total_widget = Widget.objects.aggregate(Sum('quantity'))['quantity__sum']
    return render(request, 'home.html',{'widget_list':widget_list,'widget_form':widget_form,'total_widget':total_widget})

def add_widget(request):
  # create a ModelForm instance using the data in request.POST
  form = WidgetForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    new_widget= form.save(commit=False)
    new_widget.save()
  return redirect('/')

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'