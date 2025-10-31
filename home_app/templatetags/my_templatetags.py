from django import template

register = template.Library()


@register.simple_tag
def show_result(value):
    """Return the given value for inline rendering.

    Use this as: {% show_result 'some text' %} or
    {% show_result some_variable %}.
    """
    return value
