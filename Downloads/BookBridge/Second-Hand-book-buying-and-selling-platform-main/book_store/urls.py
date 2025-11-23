from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import re_path
from . import views
from .views import Login, Cart, Checkout,Cart1, Orders, SellView

urlpatterns = [
    re_path('^$', views.index, name='index1'),
    re_path('login', Login.as_view(), name='login'),
    re_path('logout', views.logout, name='logout'),
    re_path('signup', views.signup, name='signup'),
    re_path('shop', views.shop, name='shop'),
    #url('shop', Shop.as_view(), name='shop'),
    re_path('about', views.about, name='about'),
    re_path('view_p/(?P<my_id>\d+)/$', views.single, name='single_product'),
    re_path('cart', Cart.as_view(), name='cart'),
    re_path('checkout', Checkout.as_view(), name='checkout'),
    re_path('order', Orders.as_view(), name='orders'),
    re_path('sell', views.sell, name='sell'),
    #url('image' , views.Image , name='selling'),
    re_path('sview', SellView.as_view(), name="sell_view"),
    #url('pay',views.pay, name='payment'),
    #url('summary', views.summary,name = 'summary'),
    #url('cart/(?P<my_id>\d+)/$', Cart1.as_view(), name='remove'),
    re_path('success', views.success, name='success'),
    re_path('feedback', views.feedback, name='feedback'),
    re_path('forgot', views.forgot , name='forgot'),
    re_path('home',views.home,name='home'),


    path('reset_password',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name='password_reset'),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name='password_reset_complete')

]