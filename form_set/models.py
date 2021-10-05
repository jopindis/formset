from django.db import models

# Create your models here.



class Customer(models.Model):

    name=models.CharField(max_length=200,null=True)



    def __str__(self):
        return str(self.name)



class Book(models.Model):

    name=models.CharField(max_length=200,null=True)
    rate=models.DecimalField(max_digits=9, decimal_places=2)


    
    def __str__(self):
        return self.name

class Invoice(models.Model):

    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    total=models.DecimalField(max_digits=9, decimal_places=2)


    def __str__(self):
        return str(self.customer)
class Lineitem(models.Model):
    customer=models.ForeignKey(Customer, related_name='customer',on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Book,related_name='product',on_delete=models.SET_NULL,null=True)
    rate=models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
