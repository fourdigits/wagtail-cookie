from django import template

from cookie.forms import CookieForm

register = template.Library()


@register.inclusion_tag('cookie/tags/modal.html', takes_context=True)
def cookie_modal(context):
    return {
        'request': context.request,
        'form': CookieForm,
        'hide_modal': context.request.session.get('hide_modal')
    }


@register.filter
def analytical_cookies(request):
    if not request:
        return False
    return request.session.get('analytical_cookies')


@register.filter
def third_party_cookies(request):
    if not request:
        return False
    return request.session.get('third_party_cookies')
