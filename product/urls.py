from django.urls import path

from product.views import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
    category_list,
    category_detail,
    category_delete,
    category_update,
    category_create,
    supplier_list,
    supplier_detail,
    supplier_delete,
    supplier_create,
    supplier_update,
    ReviewView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewUpdateView,
    ProductImageView
    
)

urlpatterns = [
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),
    
    path(route='categories/', view=category_list, name='category_list'),
    path(route='categories/create', view=category_create, name='category_create'),
    path(route='category/<int:id>', view=category_detail, name='category_detail'),
    path(route='category/<int:id>/delete', view=category_delete, name='category_delete'),
    path(route='category/<int:id>/update', view=category_update, name='category_update'),
    
    path(route='suppliers/', view=supplier_list, name='supplier_list'),
    path(route='suppliers/create', view=supplier_create, name='supplier_create'),
    path(route='supplier/<str:name>', view=supplier_detail, name='supplier_detail'),
    path(route='supplier/<str:name>/delete', view=supplier_delete, name='supplier_delete'),
    path(route='supplier/<str:name>/update', view=supplier_update, name='supplier_update'),
    
    path(route='reviews/', view=ReviewView.as_view(), name='review_list'),
    path(route='reviews/create', view=ReviewCreateView.as_view(), name='review_create'),
    path(route='product_reviews/<int:id>', view=ReviewDetailView.as_view(), name='review_detail'),
    path(route='product/<int:id>/update', view=ReviewUpdateView.as_view(), name='review_update'),
    
    path(route='product_images/', view=ProductImageView.as_view(), name='product_images')
]
