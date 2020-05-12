from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from lists.models import Item, List

# Create your views here.


def home_page(request: HttpRequest):
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # # request.POST.get('item_text', '')
    # # 如果是以 get 方法请求，则没有传递 item_text 作为表单数据，用此方法返回空字符串，不至于报错KeyError
    # return render(request, 'home.html', {'new_item_text': item.text})
    return render(request, 'home.html')


def view_list(request: HttpRequest):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request: HttpRequest):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world')
