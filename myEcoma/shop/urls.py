from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='ShopName'),
   path('about/',views.about,name='AboutUs'),
   path('contact/',views.contact,name='ContactUs'),
   path('search/',views.search,name='Search'),
   path('products/',views.products,name='ProductView'),
   path('checkout/',views.checkout,name='CheckOut'),
   path('tracker/',views.tracker,name='Treaking'),
   path('cart/',views.cart,name='cart'),
   path("products/<int:myid>", views.productView, name="ProductView"),








]
