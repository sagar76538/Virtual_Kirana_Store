import email
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django.contrib.auth.hashers import check_password
from store.models.contact import Contacts
from django.views import View
# from store.models.product import Products
# from store.models.orders import Order


class Contact(View):
    def get(self, request):
       return render(request, 'contact.html')

    def post(self,request):
       if request.method == 'POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         # sub=request.POST.get('sujbect')
         msg=request.POST.get('msg')
         # pic=request.POST.get('pic')

         con=Contacts(name=name,email=email,msg=msg)
         con.save()
         return redirect('contact')
      
      