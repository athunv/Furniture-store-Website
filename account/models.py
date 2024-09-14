from django.db import models
from django.contrib.auth.models import User

    

class Product(models.Model):

    
    product_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    option=(
        ('Bed and Matress','Bed and Matress'),
        ('Cofee Table', 'Coffe Table'),
        ('Cupboards','Cupboards'),
        ('Office Chairs','Office Chairs'),
        ('Sofa','sofa')   
    )
    category = models.CharField(max_length=100, choices=option)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.product_name
    


class Cart(models.Model):

    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

  

class Order(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300)
    phone= models.IntegerField()
    options=(
        ('order placed','order placed'),
        ('shipped','shipped'),
        (' out for delivery','out for delivery'),
        ('delivered','delivered'),
    )
    status = models.CharField(max_length=100,default='order placed',choices=options)
    


   