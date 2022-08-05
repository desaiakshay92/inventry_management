from unicodedata import category
from django.db import models

# Create your models here.

class NewItem(models.Model):
    CATEGORY_CHOICE = (("FOOD_AND_DRINK","FOOD_AND_DRINK"),
    ("HOUSEKEEPING","HOUSEKEEPING"),
    ("ELECTRIC_GOODS","ELECTRIC_GOODS"),
    ("STATIONARY","STATIONARY"),
    ("SAFETY","SAFETY"),
    ("OTHER","OTHER"))

    new_item_id = models.AutoField(primary_key=True)
    new_item_name = models.CharField(max_length=100,unique=True)
    new_item_Created_Date = models.DateField(auto_now=True)
    category_name = models.CharField(max_length=100, choices=CATEGORY_CHOICE)
    # total = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.new_item_name}"

class Items(models.Model):
    
    item_id = models.AutoField(primary_key=True)
    items = models.ForeignKey(NewItem,related_name="item",on_delete=models.PROTECT)
    qty = models.IntegerField()
    shelf_life  = models.DateField(auto_now=False)
    dates = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.items}"

class DeletedItems(models.Model):
    del_items = models.OneToOneField(NewItem,on_delete=models.PROTECT)
    del_qty = models.IntegerField()
    dates = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.del_items}"
    
