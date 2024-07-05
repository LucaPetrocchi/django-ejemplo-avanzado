from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from product.repositories.product import ProductRepository
from product.models import Category, ProductReview, ProductImage
from product.repositories.category import CategoryRepository
from product.repositories.supplier import SupplierRepository
from product.repositories.reviews import ReviewRepository
from product.forms import ProductForm, ProductReviewForm, ProductImageForm


repo = ProductRepository()
catrepo = CategoryRepository()

# product views

def product_list(request):
    product_repository = ProductRepository()
    productos = product_repository.get_all()
    return render(
        request,
        'products/list.html',
        dict(
            products=productos
        )
    )

def product_detail(request, id):
    product_repository = ProductRepository()
    producto = product_repository.get_by_id(id=id)
    return render(
        request,
        'products/detail.html',
        {"product":producto}
    )

@login_required(login_url='login')
def product_update(request, id):
    product_repository = ProductRepository()
    product = product_repository.get_by_id(id)
    if request.method == 'POST':
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)
        
    
        product_repository.update(
            producto=product,
            nombre=name,
            precio=price,
            descripcion=description,
            stock=stock,
            categoria=category
        )
        
        return redirect('product_detail', product.id)
    
    categorias = Category.objects.all()
    return render(
        request,
        'products/update.html',
        dict(
            categories=categorias,
            product=product
        )
    )

def product_delete(request, id):
    product_repository = ProductRepository()
    product = product_repository.get_by_id(id)
    product_repository.delete(product)
    return redirect('product_list')

def product_create(request):
    
    form = ProductForm()
    
    product_repository = ProductRepository()
    if request.method == 'POST':
        
        # if form.is_valid()
        #   # form.save()
        #   producto_nuevo = repo.create(
        #       nombre = form.cleaned_data('name'),
        #   # etc etc con cada campo
        # )
        # return redirect ('product_list')
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)
    
        new_product = product_repository.create(
            nombre=name,
            precio=price,
            descripcion=description,
            cantidades=stock,
            categoria=category
        )
        return redirect('product_detail', new_product.id)
    categorias = Category.objects.all()
    return render(
        request, 
        'products/create.html',
        dict(
            form=form
        )
        )
    
    
class ProductView(View):#
    def get(self, request):
        product_repository = ProductRepository()
        productos = product_repository.get_all()
        return render(
            request,
            'products/list.html',
            dict(
                products=productos
            )
        )
    
class ProductDetailView(View):
    def get(self, request, id):
        product_repository = ProductRepository()
        producto = product_repository.get_by_id(id=id)
        return render(
            request,
            'products/detail.html',
            dict(
                product=producto
            )
        )
        
class ProductUpdateView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(instance=review)
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            ),
        )
    
class ProductDeleteView(View):
    def post(self, request, id):
        product_repository = ProductRepository()
        product = product_repository.get_by_id(id=id)
        product_repository.delete(product)
        return redirect('product_list')

class ProductCreateView(View):
    def post(self, request):
        product_repository = ProductRepository()
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        id_category = request.POST.get('id_category')
        category = Category.objects.get(id=id_category)
        
        new_product = product_repository.create(
            nombre=name,
            precio=price,
            descripcion=description,
            cantidades=stock,
            categoria=category,
        )
        
        return redirect(
            'product_detail',
            new_product.id
        )

    def get(self, request):
        categorias = Category.objects.all()
        return render(
            request,
            'products/create.html',
            dict(
                categories=categorias
            )
        )

# category views

def category_list(request):
    category_repository = CategoryRepository()

    categorias = category_repository.get_all()
    return render(
        request,
        'categories/list.html',
        dict(
            categories=categorias
        )
    )
    
def category_detail(request, id: int):
    category_repository = CategoryRepository()
    # product_repository = ProductRepository()
    categoria = category_repository.get_by_id(id)
    # productos = product_repository.filter_by_category(categoria=categoria)
    return render(
        request,
        'categories/detail.html',
        dict(
            category=categoria, 
            # products=productos,
        )
    )
    
def category_delete(request, id: int):
    category_repository = CategoryRepository()
    categoria = category_repository.get_by_id(id)
    category_repository.delete(categoria)
    return redirect('category_list')

def category_update(request, id: int):
    category_repository = CategoryRepository()
    categoria = category_repository.get_by_id(id)
    if request.method == 'POST':
        nombre = request.POST.get('name')
    
        category_repository.update(categoria, nombre)
        
        return redirect('category_list')
    return render(
        request,
        'categories/update.html',
        dict(category=categoria)
    )

def category_create(request):
    category_repository = CategoryRepository()
    if request.method == 'POST':
        nombre = request.POST.get('name')
    
        category_repository.create(nombre)
        
        return redirect('category_list')
    return render(
        request,
        'categories/create.html',
    )
    
# supplier views

def supplier_list(request):
    supplier_repo = SupplierRepository()
    suppliers = supplier_repo.get_all()
    return render(
        request,
        'suppliers/list.html',
        dict(
            suppliers=suppliers
        )
    )
    
def supplier_detail(request, name):
    supplier_repo = SupplierRepository()
    supplier = supplier_repo.get_by_name(name)
    return render(
        request,
        'suppliers/detail.html',
        dict(
            supplier=supplier
        )
    )

def supplier_update(request, name):
    supplier_repo = SupplierRepository()
    supplier = supplier_repo.get_by_name(name)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        supplier_repo.update(
            supplier=supplier,
            name=name,
            address=address,
            phone=phone,
        )
        
        return redirect('supplier_detail', supplier.name)
    
    return render(
        request,
        'suppliers/update.html',
        dict(
            supplier=supplier,
        )
    )
    
def supplier_delete(request, name):
    supplier_repo = SupplierRepository()
    supplier = supplier_repo.get_by_name(name)
    supplier_repo.delete(supplier)
    return redirect('supplier_list')

    
def supplier_create(request):
    supplier_repo = SupplierRepository()
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        new_supplier = supplier_repo.create(
            name=name,
            address=address,
            phone=phone,
        )
        
        return redirect('supplier_detail', new_supplier.name)
    
    return render(
        request,
        'suppliers/create.html',
    )
    
# review views

class ReviewView(View):
    def get(self, request):
        rerepo = ReviewRepository()
        reviews = rerepo.get_all()
        if request.user.is_authenticated and not request.user.is_staff:
            reviews = reviews.filter(author=request.user)
        return render(
            request,
            'product_reviews/list.html',
            dict(
                reviews=reviews
            )
        )
    
class ReviewDetailView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        return render(
            request,
            'product_reviews/detail.html',
            dict(
                review=review
            )
        )
    
class ReviewUpdateView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(instance = review)
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )
        
    def post(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_reviews')
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )
        
        # rerepo = ReviewRepository()        
        
        # review = rerepo.get_by_id(id=id)
        
        # product_id = request.POST.get('product_id')
        # text = request.POST.get('text')
        # rating = request.POST.get('rating')
        
        # # product = product_repository.get_by_id(id=product_id)
        
        # review.text = text
        # review.rating = rating
        # review.save()
        
        # return redirect('review_detail', review.id)        
    
class ReviewCreateView(View):
    def get(self, request):
        product_repository = ProductRepository()
        products = product_repository.get_all()
        
        return render(
            request,
            'product_reviews/create.html',
            dict(
                products=products,
            )
        )
        
    def post(self, request):
        rerepo = ReviewRepository()
        product_repository = ProductRepository()
        
        product_id = request.POST.get('id_product')
        text = request.POST.get('review')
        rating = request.POST.get('rating')        
        author = request.user
        
        product = product_repository.get_by_id(product_id)
        
        rerepo.create(
            product=product,
            author=author,
            text=text,
            rating=rating
        )
        
        return redirect('review_list')
                
class ProductImageView(View):
    def get(self, request):
        images = ProductImage.objects.all()
        return render(
            request,
            'product_images/list.html',
            dict(
                images=images
            )
        )