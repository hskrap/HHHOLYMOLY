from django.shortcuts import render
from django.http import HttpResponse
from login.models import Info

def index(request):
    display='none'
    data=0
    return render(request, 'home/home.html', { 'display' : display , 'data' : data})

def test(request):
    search_text=request.POST.get('search')
    obj=Info.objects.all()

    for object in obj:
        no_data=object.no
        if search_text == no_data:
            name_date=object.name
            data=0
            return render(request, 'home/home.html', {'no': no_data ,'name': name_date, 'data' : data})
        else:
            display='none'
            data=1
            return render(request, 'home/home.html', {'alert': '데이터가 없습니다', 'display': display , 'data': data})

