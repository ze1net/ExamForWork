from django import template
from django.urls import resolve, reverse
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, name):
    menu_items = MenuItem.objects.filter(menu__name=name)
    current_url = resolve(context['request'].path_info).url_name
    current_item = None
    item_parents = []

    # Find the current menu item, based on the current URL
    for item in menu_items:
        if item.url == current_url or item.url == reverse(current_url):
            current_item = item
            # Add all the parent items to item_parents
            parent = item.parent
            while parent is not None:
                item_parents.insert(0, parent)
                parent = parent.parent
            break

    # If no current item was found, default to the first item in the menu
    if current_item is None and menu_items:
        current_item = menu_items[0]

    # Render the menu using the menu_item.html template
    return template.loader.render_to_string('menu/menu_item.html', {
        'menu_items': menu_items,
        'current_item': current_item,
        'item_parents': item_parents,
    })
