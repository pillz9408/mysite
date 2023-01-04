from django.shortcuts import render
#추가
from django.http import HttpResponse

# Create your views here.
#추가
def index(request):
    return HttpResponse("pybo App에 오신것을 환영합니다.")
