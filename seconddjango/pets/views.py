from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Turtle
from django.views import View
from .helpers import GetBody
# Import serializer (turns something into another thing) to turn objects in JSON strings
from django.core.serializers import serialize


# Create your views here.

# Views classes structure
# ex. dog model
# /dog - (get (index), post (create))
# /dog/:id - (get (show), put (update), delete (destroy))

class TurtleView(View):
    ## Index
    def get(self, request):
        # save all turtles objects in a var (an array)
        all = Turtle.objects.all()
        # use serializer to turn obj (bc rn they are just pure objects, not dictionaries yet) into JSON string
        serialized = serialize("json", all)
        # turn json strings back into dictionaries
        # bc JsonResponse takes dictionaries
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)
    
    ## Create
    def post(self, request):
        # get the req body
        body = GetBody(request)
        print(body)
        # cant use dot notation bc body is a dictionary, not a pure object
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        # serialize turtle obj into json and then into dict
        # pass turtle as an array bc thats what serialize() expects
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
    
    
class TurtleViewID(View):
    ## Show
    def get(self, request, id):
        # get turtle
        turtle = Turtle.objects.get(id=id)
        # serialize turtle
        finalData = json.loads(serialize("json", [turtle]))
        # return dict
        return JsonResponse(finalData, safe=False)
    ## Update
    def put(self, request, id):
        # get req body
        body = GetBody(request)
        
        ## update
        ## **: unpackaging operator: unpacks dictionary and turns it into separate arguments
        ## tells update function to update each property
        Turtle.objects.filter(id=id).update(**body)
        
        # get updated turtle from db
        turtle = Turtle.objects.get(id=id)
        # serialize it
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
        
    ## Delete
    def delete(self, request, id):
        # get turtle
        turtle = Turtle.objects.get(id=id)
        # delete turtle
        turtle.delete()
        # serialize and return the deleted turtle
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
        