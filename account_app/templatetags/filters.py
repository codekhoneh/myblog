from django import template
import datetime

register = template.Library()

def cutter(value, arg):
    """Truncate the string to the given length (arg may be a string)."""
    try:
        n = int(arg)
    except (TypeError, ValueError):
        return value
    return value[:n]

register.filter('mytruncate', cutter)


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)