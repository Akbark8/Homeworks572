from django.http import HttpResponse
import datetime, random

def current_time(request):
    return HttpResponse(f"⏰ Текущее время: {datetime.datetime.now()}")

def random_number(request):
    return HttpResponse(f"🎲 Случайное число: {random.randint(1,100)}")

def about_me(request):
    return HttpResponse("👋 Привет, меня зовут [ТВОЁ_ИМЯ], я изучаю Django!")
