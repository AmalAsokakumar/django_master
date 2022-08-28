from django.shortcuts import render
from .models import Post

# posts = [
#      {
#           'author': 'Bimal Jalal',
#           'title':'The India Story',
#           'content': 'Based on extensive research and data, and aided by Bimal Jalan experience as the former Governor of the Reserve Bank of India, this book gives us a vision for the way ahead. Since 2014, the political profile of the Indian Union government has changed dramatically. ...',
#           'date_posted':'2022',
#      },
#      {
#           'author': 'Ruskin Bond',
#           'title':'Listen to Your Heart: The London Adventure',
#           'content': 'I followed my heart instead of my head. It is something I have done all my life. Shortly before his eighteenth birthday, Ruskin embarks on a literary journey and reaches England after charting unknown waters. ... ',
#           'date_posted':'2022',
#      }
#      ]

# Create your views here.
def home(request):
     context ={
          
                    #'posts':posts
                    'posts': Post.objects.all(),
               
               }     
     return render(request, 'blog/home.html', context)
     
def about(request):
     return render(request, 'blog/about.html')

