from django.shortcuts import render, HttpResponse, render_to_response
from items.models import Product, ProductImage
from django.http import JsonResponse
from django.views import View

class ESearchView(View):
    template_name = 'search/search.html'

    def get(self, request, *args, **kwargs):
        
        question = request.GET.get('q')
        
        if question is not None:
            question = question.lower()
            search_products = Product.objects.filter(name__contains=question[1:])
            search_results = []
            for product in search_products:
                search_results.append(ProductImage.objects.get(is_main=True, product=product))
            # image_urls = {}
            # for result in search_results:
            #     image_urls[result.id] = ProductImage.objects.get(product=result, is_main=True).image.url
            # print(image_urls)    
            last_question= '?q=%s' % question

        return render(request, 'search/search.html', locals())



