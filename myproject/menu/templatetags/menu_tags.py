from django import template
from menu.models import Item

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu):
    selected_item_id = int(context['request'].GET.get(menu, 0))
    items = Item.objects.filter(menu__title=menu).values()
    menu_tree = build_menu_tree(
        items, parent_id=None, selected_item_id=selected_item_id)

    return {
        'items': menu_tree,
        'active_id': selected_item_id,
        'menu': menu,
        'other_querystring': get_querystring(context, menu)
    }


def build_menu_tree(items, parent_id, selected_item_id):
    tree = []
    for item in items:
        if item['parent_id'] == parent_id:
            item['is_active'] = item['id'] == selected_item_id
            item['child_items'] = build_menu_tree(items, item['id'], selected_item_id)
            item['is_expanded'] = item['is_active'] or any(
                child['is_expanded'] for child in item['child_items'])
            tree.append(item)
    return tree


def get_querystring(context, menu):
    querystring_args = [
        f"{key}={value}"
        for key, value in context['request'].GET.items()
        if key != menu
    ]
    return '&'.join(querystring_args)
