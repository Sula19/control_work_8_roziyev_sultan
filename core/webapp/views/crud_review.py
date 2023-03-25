from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from webapp.models import Review, Product
from webapp.forms import ReviewForm
from django.shortcuts import redirect, get_object_or_404


class CreateReview(LoginRequiredMixin, CreateView):
    template_name = 'review/add_review.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        form.save()
        return redirect('detail_product', pk=self.kwargs.get('pk'))


class UpdateReview(UserPassesTestMixin, UpdateView):
    template_name = 'review/update_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user or self.request.user.groups.filter(name__in=['moderators', 'admins']).exists()


class DeleteReview(UserPassesTestMixin, DeleteView):
    model = Review

    def post(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        review.delete()
        return redirect('/')

    def test_func(self):
        user = self.get_object()
        return user.author == self.request.user or self.request.user.groups.filter(name__in=['moderators', 'admins']).exists()
