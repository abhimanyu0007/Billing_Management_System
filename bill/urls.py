from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/',views.loginPage,name='loginPage'),
    path('logout/',views.logoutUser,name='logout'),
    path('products/',views.products,name='products'),
    path('customers/',views.customers,name='customers'),
    path('billing/',views.billing,name='billing'),
    path('receipt/<str:pk>',views.receipt,name='receipt'),
    path('contacts/',views.contacts,name='contacts'),

]
