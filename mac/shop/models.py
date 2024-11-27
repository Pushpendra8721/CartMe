from django.db import models

# Create your models here........................
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    productdsc = models.CharField(max_length=3000)
    chategorie=models.CharField(max_length=500,default="")
    subchategorie=models.CharField(max_length=500,default="")
    price=models.IntegerField(default="0")
    pubdate = models.DateField()
    imgage=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    masg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300,default="")
    phone = models.CharField(max_length=10,default="")
    desc = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=1000,default="")
    name = models.CharField(max_length=50)
    amount=models.IntegerField(default=0)
    email = models.CharField(max_length=300,default="")
    phone = models.CharField(max_length=10,default="")
    address = models.CharField(max_length=1000,default="")
    zip_code = models.CharField(max_length=1000,default="")
    state = models.CharField(max_length=1000,default="")
    city = models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
