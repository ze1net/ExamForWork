from django.shortcuts import render, get_object_or_404
from django.urls import resolve, reverse
from .models import MenuItem


def menu_page(request, name):
    menu_items = MenuItem.objects.filter(menu__name=name)
    current_url = resolve(request.path_info).url_name
    current_item = None

    # Find the current menu item, based on the current URL
    for item in menu_items:
        if item.url == current_url or item.url == reverse(current_url):
            current_item = item
            break

    context = {
        'menu_items': menu_items,
        'current_item': current_item,
    }
    return render(request, 'menu/menu_page.html', context)
