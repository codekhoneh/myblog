from django import template

register = template.Library()


@register.inclusion_tag('home_app/result.html')
def show_result(objects):
    """Render the given iterable into the result partial.

    Usage: {% show_result some_iterable %}
    The inclusion template expects a context variable named 'objects'.
    """
    # If a string was passed (e.g. {% show_result "text" %}),
    # treat it as a single object to avoid iterating characters.
    if objects is None:
        objs = []
    elif isinstance(objects, str):
        objs = [objects]
    else:
        try:
            iter(objects)
            objs = objects
        except TypeError:
            objs = [objects]
    return {'objects': objs}



