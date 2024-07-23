from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def test_connection(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT DATABASE()")
        row = cursor.fetchone()
    return HttpResponse(f"Connected to database: {row[0]}")
# Create your views here.
