from django import template

register = template.Library()


@register.simple_tag
def show_result(value):
    """Return the given value for inline rendering.

    Use this as: {% show_result 'some text' %} or
    {% show_result some_variable %}.
    """
    return value


@register.inclusion_tag('home_app/result.html', takes_context=True)
def render_results(context):
    """Inclusion tag that renders `result.html` with recent articles.

    It looks for `recent_art` in the current template context and passes it
    into the inclusion template as `objects`.
    """
    recent = context.get('recent_art')
    return {'objects': recent}
