from typing import OrderedDict
from django.shortcuts import render
from rest_framework import viewsets
from consumables.serializer import ItemSerilizer,NewItemSerilizer,DeletedItemSerializer
from consumables.models import Items, NewItem, DeletedItems
from rest_framework.response import Response
from collections import OrderedDict
from json import dumps,loads
from consumables.utility import total_count
from rest_framework.decorators import api_view
from rest_framework.decorators import action
# Create your views here.

class NewItemView(viewsets.ViewSet):
    def list(self,request,pk):
        newitem_data = NewItem.objects.get(pk=pk)
        newitem_serializer = NewItemSerilizer(newitem_data)
        dict_data = loads(dumps(newitem_serializer.data))
        count = total_count(dict_data)
        deleted_data = DeletedItems.objects.get(del_items=dict_data['new_item_id'])
        deleted_serializer = DeletedItemSerializer(deleted_data)
        dict_data = deleted_serializer.data
        deleted_count = dict_data['del_qty']
        count = count-deleted_count
        return Response({"Data":newitem_serializer.data,"Total":count})


    def create(self, request):
        newitem_data = request.data
        # newitem_data = NewItem.objects.all()
        newitem_serializer = NewItemSerilizer(data=newitem_data)
        if newitem_serializer.is_valid():
            newitem_serializer.save()
            return Response({"Message":"New Item Registered Successfully"})
        else:
            return Response({"Error":newitem_serializer._errors})

    def destroy(self,request,pk=None):
        qty_del = request.data
        newitem_data = NewItem.objects.get(pk=pk)
        newitem_serializer = NewItemSerilizer(newitem_data)
        dict_data = loads(dumps(newitem_serializer.data))
        count = total_count(dict_data)
        if count < 0:
            return Response({"Error":"No Items To Consume"})
        else:
            count = int(count)-int(qty_del['del_qty'])
            return Response({"Updated_Count":count,"Data":newitem_serializer.data})
        # if newitem_serializer:
        # for i in newitem_serializer.data:
        #     dict_data = loads(dumps(i))
        #     count = total_count(dict_data)
        #     # requested_data.append({"total":count})
        #     requested_data['total'] = int(count)
        #     serializer = NewItemSerilizer(data=requested_data)
        #     if serializer.is_valid():
        #         serializer.save()
        #     else:
        #         return Response({"Error":serializer._errors})
        #     return Response(serializer.data)
        # else:
        #     newitem_serializer = NewItemSerilizer(data=requested_data)
        #     if newitem_serializer.is_valid():
        #         newitem_serializer.save()
        #         newitem_data = NewItem.objects.all()
        #         newitem_serializer = NewItemSerilizer(newitem_data,many=True)
        #         # if newitem_serializer:
        #         for i in newitem_serializer.data:
        #             dict_data = (loads(dumps(i)))
        #             count = total_count(dict_data)
        #             requested_data['total'] = count
        #             serializer = NewItemSerilizer(data=requested_data)
        #             if serializer.is_valid():
        #                 serializer.save()
        #                 return Response(serializer.data)
        #             else:
        #                 return Response(serializer._errors)
        #     else:
        #         return Response({"Error":newitem_serializer._errors})
        

            

    
    # serializer_class = NewItemSerilizer
    # queryset = NewItem.objects.all()


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerilizer
    queryset = Items.objects.all()




@api_view(['GET'])
def DeletedItemView(request,pk):
    newitem_data = NewItem.objects.get(pk=pk)
    newitem_serializer = NewItemSerilizer(newitem_data)
    dict_data = loads(dumps(newitem_serializer.data))
    count = total_count(dict_data)
    if count<0:
        return Response({"Message":"No Items Available To Consume"})
    else:
        deleted_data = request.data
        if deleted_data['del_qty'] > count:
            return Response({"Message":"Quantity Is Not Sufficient"})
        else:
            deleted_data_serializer = DeletedItemSerializer(data=deleted_data)
            if deleted_data_serializer.is_valid():
                deleted_data_serializer.save()
                return Response({"Message":"Deleted Data Inserted Successfully"})
            else:
                return Response({"Error":deleted_data_serializer._errors})
# class DeletedItemView(viewsets.ViewSet):
#     def list(self,request,pk):
#         
#         return Response({"Data":newitem_serializer.data,"Total":count})

#     def create(self, request):
#         newitem_data = NewItem.objects.get(pk=pk)
#         newitem_serializer = NewItemSerilizer(newitem_data)
#         dict_data = loads(dumps(newitem_serializer.data))
#         count = total_count(dict_data)
        
#         newitem_data = request.data
#         # newitem_data = NewItem.objects.all()
#         newitem_serializer = NewItemSerilizer(data=newitem_data)
#         if newitem_serializer.is_valid():
#             newitem_serializer.save()
#             return Response({"Message":"Deleted Entry Created"})
#         else:
#             return Response({"Error":newitem_serializer._errors})
    # def list(self,request):
    #     newitem_data = NewItem.objects.all()
    #     newitem_serializer = NewItemSerilizer(newitem_data,many=True)
    #     return Response(newitem_serializer.data)

    # def create(self, request):
    #     newitem_data = NewItem.objects.get()
    #     newitem_data = request.data
    #     # newitem_data = NewItem.objects.all()
    #     newitem_serializer = NewItemSerilizer(data=newitem_data)
    #     if newitem_serializer.is_valid():
    #         newitem_serializer.save()
    #         return Response({"Message":"New Item Registered Successfully"})
    #     else:
    #         return Response({"Error":newitem_serializer._errors})

