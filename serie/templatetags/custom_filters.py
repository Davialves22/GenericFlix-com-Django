# serie/templatetags/custom_filters.py
from django import template

register = template.Library()


@register.filter
def get_model_name(obj):
    """Retorna o nome da classe do modelo (ex: 'Filme', 'Serie')."""
    if obj is None:
        return ''
    # Isso pega o nome da classe do objeto (ex: Serie ou Filme)
    return obj.__class__.__name__
