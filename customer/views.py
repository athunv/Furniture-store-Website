
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from account.models import Product,Cart,Order
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail
from  datetime import date
from .forms import *
from django.urls import reverse_lazy



# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.info(request,'Please Login')
            return redirect('login')
    return inner

decorators = [signin_required,never_cache]

# Create your views here.
class Homeview(ListView):

    template_name='userhome.html'
    queryset = Product.objects.all()
    context_object_name = 'products'


@method_decorator(decorators,name='dispatch')
class ProductDetilView(DetailView):

    template_name='details.html'
    model = Product
    context_object_name ='product'
    pk_url_kwarg = 'id'

decorators
def AddToCart(request,*args,**kwargs):

    pid = kwargs.get('id')
    product= Product.objects.get(id=pid)
    user = request.user
    try:
        cart = Cart.objects.get(user=user,product=product)
        messages.info(request,"Product already extists in cart")
        return redirect('userhome')

    except:
        Cart.objects.create(user=user,product=product)
        messages.success(request,"Product added to cart")
        return redirect('cartlist')

@method_decorator(decorators,name='dispatch')    
class CartListView(ListView):
    template_name = 'cart.html'
    queryset = Cart.objects.all()
    context_object_name='cartitems'

    def get_queryset(self) :
        qs= super().get_queryset()
        qs.filter(user=self.request.user)
        return qs

decorators   
def removeCartitems(request,*args,**kwargs):

    cid=kwargs.get('id')
    cart = Cart.objects.get(id=cid)
    cart.delete()
    messages.success(request,"Product removed from cart")
    return redirect('cartlist')

@method_decorator(decorators,name='dispatch')
class Checkoutview(TemplateView):

    template_name= 'checkout.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        cid = kwargs.get('id')
        cart= Cart.objects.get(id=cid)
        context['product']=cart.product
        return context
    
    def post(self,request,*args,**kwargs):
        
        cid = kwargs.get('id')
        cart= Cart.objects.get(id=cid)
        product = cart.product
        user = request.user
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Order.objects.create(user=user,product=product,address=address,phone=phone)
        cart.delete()

        # send_mail
        subject = 'Order Conformation'
        msg = f'Order for {product.product_name} is Conformed Successfully on {date.today()}'
        from_id = 'athunv856@gmail.com'
        to_id = [user.email]
        send_mail(subject,msg,from_id,to_id)

        messages.success(request,"Order placed successfully")
        return redirect('olist')
    
@method_decorator(decorators,name='dispatch')
class BedView(ListView):
    template_name = 'items.html'
    context_object_name = 'products'  

    def get_queryset(self):
        return Product.objects.filter(category='Bed and Matress')
    
@method_decorator(decorators,name='dispatch')
class CTableView(ListView):
    template_name = 'items.html'
    context_object_name = 'products'  

    def get_queryset(self):
        return Product.objects.filter(category='Cofee Table')
    
@method_decorator(decorators,name='dispatch')
class SofaView(ListView):
    template_name = 'items.html'
    context_object_name = 'products'  

    def get_queryset(self):
        return Product.objects.filter(category='Sofa')
    
@method_decorator(decorators,name='dispatch')   
class CupboardsView(ListView):

    template_name ='items.html'
    context_object_name= 'products'

    def get_queryset(self):
        return Product.objects.filter(category='Cupboards')

@method_decorator(decorators,name='dispatch')   
class ChairView(ListView):

    template_name = 'items.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category='Office Chairs')

@method_decorator(decorators,name='dispatch')   
class AllView(ListView):

    template_name = 'items.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

@method_decorator(decorators,name='dispatch')
class OrderView(ListView):
    template_name = 'orderlist.html'
    context_object_name = 'orders'
    queryset = Order.objects.all()

decorators   
def ordercancel(request,**kwargs):

    oid = kwargs.get('id')
    order = Order.objects.get(id=oid)
    order.delete()
    return redirect('olist')





#Seller side

@method_decorator(decorators,name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'seller.html'
    success_url = reverse_lazy('productlist')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        messages.success(self.request, 'Product added successfully')
        return super().form_valid(form)
    
@method_decorator(decorators,name='dispatch')
class UserProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    

@method_decorator(decorators,name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit.html'
    success_url = reverse_lazy('productlist')

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

@method_decorator(decorators, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_list.html'
    success_url = reverse_lazy('productlist')

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)