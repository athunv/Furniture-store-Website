from django.urls import path
from .views import *



urlpatterns = [
    path('',Homeview.as_view(),name='userhome'),
    path('detail/<int:id>',ProductDetilView.as_view(),name='detail'),
    path('addtocart/<int:id>',AddToCart,name='addtocart'),
    path('cart',CartListView.as_view(),name='cartlist'),
    path('removecart/<int:id>',removeCartitems,name='remcart'),
    path('check/<int:id>',Checkoutview.as_view(),name='checkout'),
    path('itemlist',BedView.as_view(),name='bed'),
    path('ctable',CTableView.as_view(),name='ctable'),
    path('sofa',SofaView.as_view(),name='sofa'),
    path('Cupboards',CupboardsView.as_view(),name='Cupboards'),
    path('chair',ChairView.as_view(),name='chair'),
    path('all',AllView.as_view(),name='all'),
    path('orderlist',OrderView.as_view(),name='olist'),
    path('odelete/<int:id>/', ordercancel, name='ordelete'),

    #seller

    path('addproduct',ProductCreateView.as_view(),name='addproduct'),
    path('productlist',UserProductListView.as_view(),name='productlist'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
   
]