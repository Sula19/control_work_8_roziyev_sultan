from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from webapp.models import Product
from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from webapp.forms import ProductForm
from django.shortcuts import redirect


class GroupPermission(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['moderators', 'admins']).exists()


class IndexProduct(ListView):
    template_name = 'product/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 10
    paginate_orphans = 1


class DetailProduct(DetailView):
    template_name = 'product/detail_product.html'
    model = Product


class CreateProduct(GroupPermission, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    groups = ['moderators', 'admins']

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        context = {'form': form}
        return self.render_to_response(context)


class UpdateProduct(GroupPermission, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductForm
    groups = ['moderators', 'admins']
    success_url = '/'


class DeleteProduct(PermissionRequiredMixin, DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_project'
    groups = ['moderators', 'admins']
    success_url = '/'
