import json

from rest_framework.decorators import api_view
from rest_framework import status, response

from django.http import HttpResponse

from .models import Category, Blog


@api_view()
def categories(request):
    categories = Category.objects.all()
    data = [{'title': category.title, 'slug': category.slug} for category in categories]
    return HttpResponse(
        json.dumps(data),
        #content_type = 'application/json'
    )
    # return response.Response(
    #     {'data': 'Cool'}
    # )