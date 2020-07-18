from django.shortcuts import render
from .models import login, student
import json
from django.http import JsonResponse
from queries.models import queries
# Create your views here.


def logins(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        lib_id = data["lib_id"]
        password = data["password"]
        if lib_id[0] == 'F':
            bool_check = login.objects.filter(
                lib_id=lib_id, password=password).exists()
            if bool_check:
                details = list(login.objects.filter(
                    lib_id=lib_id).values('name'))
                response = {"status": "teacher logged in",
                            "data_teach": details}
            else:
                response = 'Invalid Credentials'
        else:
            bool_check = student.objects.filter(
                lib_id=lib_id, password=password, status="active").exists()
            if bool_check:
                details = list(student.objects.filter(
                    lib_id=lib_id).values('lib_id', 'name', 'father_name', 'course', 'mobile_no', 'sec', 'email'))
                response = {"status": "student logged in",
                            "data_stud": details}
            else:
                response = 'Invalid Credentials'

    return JsonResponse(response, safe=False)


def addstudent(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        name = data['name']
        father_name = data['father_name']
        lib_id = data['lib_id']
        course = data['course']
        mobile_no = data['mobile_no']
        branch = data['branch']
        sec = data['sec']
        email = data['email']
        # password = data['password']
        bool_already_exists = student.objects.filter(
            lib_id=lib_id, mobile_no=mobile_no, email=email).exists() or student.objects.filter(
            lib_id=lib_id).exists() or student.objects.filter(
            mobile_no=mobile_no).exists() or student.objects.filter(
            email=email).exists()
        if bool_already_exists:
            response = "User already exists"
        else:
            student.objects.create(
                name=name, father_name=father_name, lib_id=lib_id, course=course, mobile_no=mobile_no, branch=branch, sec=sec, email=email)
            response = "successful"
    return JsonResponse(response, safe=False)


# def detailsstudent(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         lib_id = data['lib_id']
#         response = list(student.objects.filter(lib_id=lib_id).values(
#             'name', 'father_name', 'course', 'branch', 'mobile_no', 'sec', 'email'))
#     return JsonResponse(response, safe=False)


def allstudents(request):
    if request.method == 'GET':
        response = list(student.objects.values('id', 'name', 'father_name',
                                               'lib_id', 'course', 'mobile_no', 'branch', 'sec', 'email'))
    return JsonResponse(response, safe=False)


def delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lib_id = data['lib_id']
        student.objects.filter(lib_id=lib_id).update(status="inactive")
        response = "Delete Successfull"
    return JsonResponse(response, safe=False)


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lib_id = data['lib_id']
        name = data['name']
        father_name = data['father_name']
        course = data['course']
        mobile_no = data['mobile_no']
        branch = data['branch']
        sec = data['sec']
        email = data['email']
        student.objects.filter(lib_id=lib_id).update(name=name, father_name=father_name,
                                                     course=course, mobile_no=mobile_no, branch=branch, sec=sec, email=email)
        queries.objects.filter(key__lib_id=lib_id).update(status="finished")
        return JsonResponse('Details Updated', safe=False)
