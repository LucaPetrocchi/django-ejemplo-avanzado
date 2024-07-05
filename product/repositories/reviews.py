from product.models import ProductReview
from typing import List
from django.contrib.auth.models import User
from product.models import Product

class ReviewRepository:
    def get_all(self) -> List[ProductReview]:
        return ProductReview.objects.all()
    
    def get_by_id(self, id) -> ProductReview:
        return ProductReview.objects.get(id=id)
    
    def create(
        self,
        product: Product,
        author: User,
        text: str,
        rating: int,
    ) -> ProductReview:        
        review = ProductReview.objects.create(
            product=product,
            author=author,
            text=text,
            rating=rating,
        )
        
        return review
    
    def update(
        self,
        review: ProductReview,
        product: Product,
        text: str,
        rating: int,
    ):        
        review.product = product
        review.text = text
        review.rating = rating
        
        review.save()
        
        
