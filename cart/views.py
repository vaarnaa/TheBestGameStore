from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from core.models import Game
from .cart import Cart
from .forms import CartAddGameForm


@require_POST
def cart_add(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    form = CartAddGameForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(game=game,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, game_id):
    cart = Cart(request)
    game = get_object_or_404(Game, id=game_id)
    cart.remove(game)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddGameForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
