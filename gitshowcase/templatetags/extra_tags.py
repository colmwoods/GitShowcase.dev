from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Allow access to a dictionary item by key inside templates."""
    return dictionary.get(key)
