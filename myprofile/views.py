from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timezone
import requests

# Create your views here.

@api_view(["GET"])
def get_me(request):
    now = datetime.now(timezone.utc)
    fnow = now.isoformat()

    try:
        r = requests.get("https://catfact.ninja/fact", timeout=5)
        cat_fact = r.json()["fact"]
    except:
        cat_fact = "Unable to fetch cat fact at this time"


    response = {
            "status": "success",
            "user": {
                "email": "torohkiss@gmail.com",
                "name": "Etoro Umoren",
                "stack": "django"
            },
            "timestamp": fnow,
            "fact": cat_fact
    }

    return Response(response)
