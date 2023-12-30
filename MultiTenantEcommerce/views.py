from django.shortcuts import render
from django.views.generic import TemplateView, View
from Product.models import Product, ProductCategory
from CMS.models import Banner


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        category = ProductCategory.objects.filter(parent_category__isnull=True)
        banner = Banner.objects.all()
        ctx = {
            "prd": Product.objects.all(),
            "cat": category,
            "banners": banner
        }
        return render(request, template_name=self.template_name, context=ctx)


class SellerView(TemplateView):
    template_name = "SellerBoard/index.html"
