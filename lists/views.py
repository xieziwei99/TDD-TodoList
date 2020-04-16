from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_page(request: HttpRequest):
    # request.POST.get('item_text', '')
    # 如果是以 get 方法请求，则没有传递 item_text 作为表单数据，用此方法返回空字符串，不至于报错KeyError
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})