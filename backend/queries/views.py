from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import queries
from login.models import student
# Create your views here.


def new_query(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        lib_id = data['lib_id']
        query = data['query']
        queries.objects.create(
            query=query, key=student.objects.get(lib_id=lib_id))
    return JsonResponse('Query initiated', safe=False)


def show_active_queries(request):
    if request.method == "GET":
        response = list(queries.objects.filter(status="active").values("id", "date", "query", "key__name", 'key__father_name',
                                                                       'key__lib_id', 'key__course', 'key__mobile_no', 'key__branch', 'key__sec', 'key__email'))
    return JsonResponse(response, safe=False)


def remove_query(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        # send me id of the query
        ID = data['id']
        queries.objects.filter(id=ID).update(status="inactive")
    return JsonResponse('Query rejected', safe=False)


def accept_query(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        # send me id of the query
        ID = data['id']
        queries.objects.filter(id=ID).update(status="accepted")
        response = list(queries.objects.filter(id=ID).values("id", "date", "query", "key__name", 'key__father_name',
                                                             'key__lib_id', 'key__course', 'key__mobile_no', 'key__branch', 'key__sec', 'key__email'))
    return JsonResponse(response, safe=False)


# def show_accepted_queries(request):
#     if request.method =='GET':
#         response = list(queries.objects.filter(status="accepted").values())
#     return JsonResponse(response, safe=False)
