from django import template

register = template.Library()

MARKER = "/image/upload/"


@register.filter
def optimized(url, params="c_limit,w_1600/q_auto/f_auto"):
    if not url or MARKER not in url:
        return url
    return url.replace(MARKER, f"{MARKER}{params}/", 1)
