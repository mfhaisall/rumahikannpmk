from django.shortcuts import render
from product.models import Ikan

def index(request):

	data = Ikan.objects.all()

	return render(request,'index.html', { "data_ikan" : data })