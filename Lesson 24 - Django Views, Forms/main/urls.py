from django.urls import path
from .views import main, add_to_cart, cart, checkout, checkout_proceed, register, sign_in, sign_out, apply_discount

urlpatterns = [
    path("", main),
    path("sign-up", register, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("sign-out", sign_out, name="sign-out"),
    path("add-to-cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("cart", cart, name="cart"),
    path("apply-discount", apply_discount, name="apply_discount"),
    path("checkout", checkout, name="checkout"),
    path("checkout/procceed", checkout_proceed, name="checkout_proceed"),
]
