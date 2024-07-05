from product.models import Category
from typing import List, Optional

class CategoryRepository:
    
    def get_all(self) -> List[Category]:
        return Category.objects.all()
    
    def get_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.get(pk=id)
    
    def delete(self, cat: Category):
        cat.delete() 
        
    def update(self, cat: Category, name: str):
        cat.name = name
        cat.save()
    
    def create(self, name: str) -> Category:
        category = Category.objects.filter(name=name)
        if category:
            return "NO!!!!!!!! OCUPADDOOOOOOOO"
        return Category.objects.create(
            name=name
        )