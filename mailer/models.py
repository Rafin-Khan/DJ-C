

from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)

    # def get_order_count(self):
    #     orders = self.orders.count()
    #     return orders

    def get_order_sum(self):
        orders = Order.objects.filter(company=self)
        return sum([x.total for x in orders])

    # class Meta:
    #     ordering = ['-id']


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()

    def get_order_count(self):
        orders = self.orders.count()
        return orders


class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(Company, related_name="orders", on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name="orders", on_delete=models.SET_NULL, blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=9)
    order_date = models.DateTimeField(null=True, blank=True)
   
    added_date = models.DateTimeField(auto_now_add=True)
    
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.order_number
