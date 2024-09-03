from django.views import View
from django.shortcuts import render, redirect
from .models import TelegramUsers
from django.http import JsonResponse



class Main(View):
    def get(self, request):
        return render(request, 'main.html')
    
class Out(View):
    def get(self, request):
        return render(request, 'out.html')