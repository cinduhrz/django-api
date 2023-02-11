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
        # save all turtles objects in a var
        all = Turtle.objects.all()
        # use serializer to turn obj (bc rn they are just pure objects, not dictionaries yet) into JSON string
        serialized = serialize("json", all)
        # turn json strings back into dictionaries
        # bc JsonResponse takes dictionaries
        finalData = json.loads(serialized)
        return JsonResponse(finalData, safe=False)