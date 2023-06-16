from django.shortcuts import render
from .models import MenuItem, SliderItem


def main(request):
    menu_items = MenuItem.objects.all()
    img_items = SliderItem.objects.all()

    return render(request, "index.html", {"menu_items": menu_items, "img_items": img_items})