from django.shortcuts import render
from django.views.generic import TemplateView, View
from Product.models import Product, ProductCategory


class HomeView(View):
    template_name = "index.html"
    model = Product

    def get(self, request):
        ctx = {
            "prd": Product.objects.all(),
            "cat": ProductCategory.objects.all()
        }
        return render(request, template_name=self.template_name, context=ctx)


class SellerView(TemplateView):
    template_name = "SellerBoard/index.html"
