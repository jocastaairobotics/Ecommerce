from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductCategory, Product, Cart
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.detail import DetailView
from .forms import ProductCategoryForm, ProductForm, CartForm
from django.views import View
from django.db.models import Q, Sum, Avg, Count
from Authentication.forms import AddressForm


class ListCategory(ListView):
    model = ProductCategory
    template_name = 'product/category/index.html'


class CreateCategory(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/category/form.html'
    success_url = "/product/category"


class UpdateCategory(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    template_name = 'product/category/form.html'
    success_url = "/product/category"


class DeleteCategory(DeleteView):
    model = ProductCategory
    fields = '__all__'
    template_name = 'product/category/delete.html'
    success_url = "/product/category"


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartForm
        return context


class FilterProduct(View):
    template_name = "search.html"

    def get(self, request):
        args = request.GET.get("query")
        pr = Product.objects.filter(Q(name__icontains=args) | Q(description__icontains=args))

        ctx = {
            "search": args,
            "products": pr
        }
        return render(request=request, template_name=self.template_name, context=ctx)


class CartView(ListView):
    model = Cart
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Cart.objects.filter(user=self.request.user).aggregate(total=Sum('product__selling_price'),
                                                                     quantity=Sum("qty"))
        context.update(data)
        context['address'] = AddressForm
        return context


class CartCreateView(CreateView):
    model = Cart
    fields = ['product', 'qty']
    template_name = "product/detail.html"
    success_url = "/product/cart"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        form.instance.user = self.request.user
        instance = super().form_invalid(form)
        return instance


class CartDelete(View):

    def get(self, request, id):
        c = Cart.objects.get(id=id)
        c.delete()
        car = Cart.objects.filter(user=request.user)
        if car:
            return redirect("/product/cart")
        else:
            return redirect("/")
