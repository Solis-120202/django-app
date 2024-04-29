from django.contrib import admin

# Register your models here.
from .models import client, product, ClientProduct, transaction_type, transaction

admin.site.register(client),
admin.site.register(product),
admin.site.register(ClientProduct),
admin.site.register(transaction_type),
admin.site.register(transaction),