from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Student
from .serializers import StudentSerializer


@api_view(['POST'])
def register_student(request):

    serializer = StudentSerializer(data=request.data)
    print(serializer,"lllllll")

    if serializer.is_valid():
        serializer.save()
        return Response({
            "message":"Student registered successfully",
            "data":serializer.data
        },status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_student(request):

    phone_number = request.data.get("phone_number")
    password = request.data.get("password")

    try:

        student = Student.objects.get(phone_number=phone_number)

        if check_password(password,student.password):

            return Response({
                "message":"Login successful",
                "data":StudentSerializer(student).data
            },status=status.HTTP_200_OK)

        else:
            return Response({
                "error":"Invalid password"
            },status=status.HTTP_400_BAD_REQUEST)

    except Student.DoesNotExist:

        return Response({
            "error":"Student not found"
        },status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:

        return Response({
            "error":str(e)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)