from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    print('Hello django!')
    # return HttpResponse('<h1>Hello django!</h1>')
    return render(request, './index.html')


def password(request):
    length = request.GET.get('length')
    input_length = request.GET.get('input-length')
    print(length, input_length)
    return render(request, './password.html', {'password': 'fstweewsgsds'})
