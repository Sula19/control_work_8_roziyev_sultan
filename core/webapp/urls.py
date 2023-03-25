from django.urls import path
from webapp.views.crud_product import (IndexProduct,
                                       DetailProduct,
                                       CreateProduct,
                                       UpdateProduct,
                                       DeleteProduct)
from webapp.views.crud_review import (CreateReview,
                                      UpdateReview,
                                      DeleteReview)

urlpatterns = [
    path('', IndexProduct.as_view(), name='index'),
    path('product/<int:pk>/detail', DetailProduct.as_view(), name='detail_product'),
    path('product/add', CreateProduct.as_view(), name='add_product'),
    path('product/<int:pk>/update', UpdateProduct.as_view(), name='update_product'),
    path('product/<int:pk>/delete', DeleteProduct.as_view(), name='delete_product'),
    path('product/<int:pk>/add_review', CreateReview.as_view(), name='add_review'),
    path('product/<int:pk>/update_review', UpdateReview.as_view(), name='update_review'),
    path('product/<int:pk>/delete_review', DeleteReview.as_view(), name='delete_review')
]
