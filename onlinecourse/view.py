from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

def logout_user(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        reviews = [
            {
                "id": 1,
                "name": "Test User",
                "dealership": dealer_id,
                "review": "Great service and friendly staff!",
                "purchase": True,
                "purchase_date": "01/01/2026",
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2024
            }
        ]
        return JsonResponse({"status": 200, "reviews": reviews})

def get_dealerships(request):
    if request.method == "GET":
        dealers = [
            {
                "id": 1,
                "city": "Austin",
                "address": "123 Main St",
                "zip": "78701",
                "state": "Texas",
                "short_name": "Austin Dealership",
                "full_name": "Austin Toyota Dealership"
            }
        ]
        return JsonResponse({"status": 200, "dealers": dealers})

def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealer = {
            "id": dealer_id,
            "city": "Austin",
            "address": "123 Main St",
            "zip": "78701",
            "state": "Texas",
            "short_name": "Austin Dealership",
            "full_name": "Austin Toyota Dealership"
        }
        return JsonResponse({"status": 200, "dealer": dealer})

def get_dealers_by_state(request, state):
    if request.method == "GET":
        dealers = [
            {
                "id": 1,
                "city": "Kansas City",
                "address": "123 Kansas St",
                "zip": "64101",
                "state": state,
                "short_name": "Kansas Dealership",
                "full_name": "Kansas Toyota Dealership"
            }
        ]
        return JsonResponse({"status": 200, "dealers": dealers})

def get_car_makes(request):
    if request.method == "GET":
        car_makes = [
            {
                "id": 1,
                "name": "Toyota",
                "description": "Japanese automaker",
                "model": "Camry"
            }
        ]
        return JsonResponse({"status": 200, "car_makes": car_makes})

def analyze_review(request, text):
    if request.method == "GET":
        # Kết quả phân tích cảm xúc giả lập (hoặc tích hợp Watson NLU nếu có)
        return JsonResponse({"status": 200, "sentiment": "positive"})