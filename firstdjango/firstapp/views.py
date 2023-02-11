from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .helpers import GetBody
# Create your views here.

# class-based view
# inherit from View class
class FirstView(View):
    # this function will run for a get request
    # functions should be named after their restful route verbs
    def get(self, request):
        return JsonResponse({"hello": "world-get"})
    
    def post(self, request):
        return JsonResponse({"hello": "world-post"})
    
    def put(self, request):
        return JsonResponse({"hello": "world-put"})
    
    def delete(self, request):
        return JsonResponse({"hello": "world-delete"})
    
    
# function-based view
def functionview(request):
    return JsonResponse({"hey": "it works"})

def templateview(request):
    return render(request, "cheese.html", {"hello": "hello world"})
   
# inherit from View class     
class SecondView(View):
    def get(self, request, param):
        # allows u to use queries
        # syntax .get(key, default if query is not specified)
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse({"param": param, "query": query, "bread": bread})
    
    def post(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse({"param": param, "query": query, "bread": bread})
    
    def put(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse({"param": param, "query": query, "bread": bread})
    
    def delete(self, request, param):
        query = request.GET.get("query", "no query")
        bread = request.GET.get("bread", "no bread")
        return JsonResponse({"param": param, "query": query, "bread": bread})
    
class ThirdView(View):
    def post(self, request):
        return JsonResponse(GetBody(request))
    
    
# Views classes structure
# ex. dog model
# /dog - (get (index), post (create))
# /dog/:id - (get (show), put (update), delete (destroy))