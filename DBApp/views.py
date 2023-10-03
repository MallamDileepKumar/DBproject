from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
class Insert(View):
    def get(self, request):
        return render(request, 'insert.html')
class Insert1(View):
    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        mft = request.POST.get('mft')
        exp = request.POST.get('exp')
        product = Product(Id=id, Name=name, Cost=cost, Mft=mft, Exp=exp)
        product.save()
        return HttpResponse("""<html><body bgcolor="lightblue"><center><h1>Inserted Successfully</h1></center></body></html>""")
class Display(View):
    def get(self, request):
        Id = request.GET.get('id')
        product = Product.objects.all()
        return render(request, 'display.html', {'product': product})
class Delete(View):
    def get(self, request):
        return render(request, 'delete.html')
class Delete1(View):
    def post(self, request):
        id = request.POST.get('id')
        product = Product.objects.get(Id=id)
        product.delete()
        return HttpResponse("""<html><body bgcolor="lightblue"><center><h1>Deleted Successfully</h1></center></body></html>""")
class Update(View):
    def get(self, request):
        return render(request, 'update.html')
class Update1(View):
    def post(self, request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        mft = request.POST.get('mft')
        exp = request.POST.get('exp')
        product = Product(Id=id, Name=name, Cost=cost, Mft=mft, Exp=exp)
        product.save()
        return HttpResponse("""<html><body bgcolor="lightblue"><center><h1>Updated Successfully</h1></center></body></html>""")


