from typing import List, Optional

from product.models import Supplier

class SupplierRepository:        
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
        
    def get_by_name(self, name: str) -> Optional[Supplier]:
        return Supplier.objects.filter(name=name).first()
        
        
    def create(
            self,
            name: str,
            address: str,
            phone: int,
    ):
        return Supplier.objects.create(
            name=name,
            address=address,
            phone=phone,
        )
    
    def delete(self, supplier: Supplier):
        return supplier.delete()
        
    def update(
        self,
        name: str,
        address: str,
        phone: str,
        supplier: Supplier,
    ):
        supplier.name = name
        supplier.address = address
        supplier.phone = phone
        
        supplier.save()