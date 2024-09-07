from rest_framework.decorators import api_view
from rest_framework import status, response

from .models import Category, Blog


@api_view()
def categories(request):
    categories = Category.objects.all()
    data = [{'title': category.title, 'slug': category.slug} for category in categories]
    return response.Response(data)


@api_view(['POST'])
def create_category(request):
    data = request.data
    # Bos mag'liwmat kelgenin tekseriw!
    if not data:
        return response.Response({'error': 'Hesh narse kiritpediniz!'}, status=status.HTTP_400_BAD_REQUEST)

    # Kerek bolg'an field di tekseriw!
    if not 'title' in data:
        return response.Response(
            {"error": "'title' field joq!"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Eger alleqashan jaratilg'an magliwmat bolsa!
    try:
        category = Category.objects.create(
            title = data['title'],
            slug = data['title'].lower().replace(" ", "-")
        )
    except Exception:
        return response.Response(
            {'error': "Bunday category alleqashan jaratilg'an"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Success!
    return response.Response(
        {
            'data': 'Category was created successfull.',
            'category': category.title
         }, 
        status=status.HTTP_201_CREATED
        )