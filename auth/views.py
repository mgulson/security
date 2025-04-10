from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

import jwt
import datetime

# Your secret key
SECRET_KEY = 'Michael-Key'


def index(request):
  return JsonResponse({"message": "Hello, world!"})

def generate_token(request):
  
  if request.user.id == None:
    return JsonResponse({"error": "User not authenticated"}, status=401)
  
  payload = {
    'user_id': request.user.id,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1) 
  }

  # Encode the token
  token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
  return JsonResponse({"token": token})


def is_authenticated(request):
  token = decodeToken(token)

  if 'user_id' in token:
    return JsonResponse({"authenticated": True})
  return JsonResponse({"authenticated": False})

def decodeToken(token):
  decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
  return decoded