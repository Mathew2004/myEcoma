from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=5000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
       return self.product_name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, default="")
    phone = models.CharField(max_length=80, default="")
    msg = models.CharField(max_length=5000)


    def __str__(self):
       return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_jeson = models.CharField(max_length=50000)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=150, default="")
    address1 = models.CharField(max_length=150, default="")
    address2 = models.CharField(max_length=150, default="")
    phone = models.CharField(max_length=80, default="")
    zip = models.CharField(max_length=80, default="")

    def __str__(self):
       return self.name


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField()

    def __str__(self):
        return self.update_desc[0:7] + "..."