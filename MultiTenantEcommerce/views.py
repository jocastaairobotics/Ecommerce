from django.views.generic import TemplateView, ListView
from Product.models import Product


class HomeView(ListView):
    template_name = "index.html"
    model = Product
