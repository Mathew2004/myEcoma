from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='BlogName'),
   path('blogpost/<int:id>',views.blogpost,name='Blogpost')
]
