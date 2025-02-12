from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from book.models import Book
from customer.models import Customer

@login_required
def view_cart(request):
    customer = get_object_or_404(Customer, username=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if not request.user.is_authenticated:
        # Redirect to login page if user is not authenticated
        return redirect('login')  

    # Get the customer associated with the logged-in user
    customer = get_object_or_404(Customer, username=request.user)  # Assuming FK relationship

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(customer=customer)
    # Get or create a cart item
    cart_item = CartItem.objects.filter(cart=cart, book=book).first()
    # If item already exists, increase quantity
    if not cart_item:
        cart_item = CartItem.objects.create(cart=cart, book=book, quantity=1)
    else:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')