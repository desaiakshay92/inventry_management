from django.contrib import admin
from consumables.models import Items,NewItem,DeletedItems
# Register your models here.

admin.site.register(Items)
admin.site.register(NewItem)
admin.site.register(DeletedItems)