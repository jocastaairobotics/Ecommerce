from django.urls import reverse
from .models import ProductCategory, Product
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.detail import DetailView
from .forms import ProductCategoryForm, ProductForm


class ListCategory(ListView):
    model = ProductCategory
    template_name = 'product/category/index.html'


class CreateCategory(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/category/form.html'


class UpdateCategory(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/category/form.html'


class DeleteCategory(DeleteView):
    model = ProductCategory
    fields = '__all__'
    template_name = 'product/category/delete.html'


class ListProduct(ListView):
    model = Product
    template_name = 'product/index.html'


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = "/product/product"


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'
    success_url = "/product/product"


class DeleteProduct(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'product/delete.html'
    success_url = "/product/product"


class ProductByCategory(ListView):
    model = Product
    template_name = "product/listing.html"

    def get_queryset(self):
        category = self.kwargs.get('category')
        qs = super().get_queryset()
        if category is not None:
            return qs.filter(category=category)
        return qs


class ProductDetails(DetailView):
    model = Product
    template_name = "product/detail.html"
