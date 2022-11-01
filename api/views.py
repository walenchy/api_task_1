from django.shortcuts import render
from django.http import JsonResponse
def getRoutes(request):
  routes =(
    {'slackUsername':'walenchy', 'backend':True, 'age':35, 'bio':'i am a backend dev intern'
		
	})
  return JsonResponse(routes, safe=False)

# Create your views here.
