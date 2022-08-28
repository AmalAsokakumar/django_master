from urllib.request import Request
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect 

# Create your views here.
def home(request):
    
     # to get cookie
     if 'login status' in request.COOKIES and 'username' in request.COOKIES:
          context= {
               'username': Request.COOKIES['username'],
               'login_status':request.COOKIES.get('login_status'),
          }
          return render(request,'home.html',context)
     else:
          return render(request,'home.html')

def login(request):
     if request.method == 'GET':
          return render(request,'login.html')
     
     if request.method == 'POST':
          username = request.POST.get('email')
          context={
               'username':username,
               'login_status':True,
          }
     response = render(request, 'home.html', context)
     #return render(request,'login.html')
     
     response.set_cookie('username', username)
     response.set_cookie('login_status', True)
     
     return response
     



def logout(request):
     response = HttpResponseRedirect(reverse('login'))
     
     response.delete_cookie('username')
     response.delete_cookie('login_status')
     
     return response