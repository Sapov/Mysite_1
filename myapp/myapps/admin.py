from django.contrib import admin
from .models import Clients, Organisation, Product, Orders

admin.site.register(Clients)
admin.site.register(Organisation)
admin.site.register(Product)
admin.site.register(Orders)

# Register your models here.
