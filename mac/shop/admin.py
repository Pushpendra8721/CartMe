from django.contrib import admin
from .models import product,Contact,Order,OrderUpdate
# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
