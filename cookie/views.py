from .forms import CookieForm
from django.views.generic.edit import FormView


class CookieView(FormView):
    template_name = 'cookie/cookie.html'
    form_class = CookieForm

    def form_valid(self, form):
        form.save(request=self.request)
        return super().form_valid(form)

    def get_initial(self):
        if self.request.user:
            return {
                'analytical_cookies': self.request.session.get('analytical_cookies', None),
                'third_party_cookies': self.request.session.get('third_party_cookies', None),
            }
        return {}

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']
