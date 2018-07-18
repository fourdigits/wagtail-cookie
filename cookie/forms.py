from django import forms


class CookieForm(forms.Form):
    CHOICES = (
        (True, 'Ja'),
        (False, 'Nee'),
    )

    analytical_cookies = forms.ChoiceField(
        label='Analytische cookies toestaan?',
        required=True,
        widget=forms.RadioSelect(),
        choices=CHOICES,
    )
    third_party_cookies = forms.ChoiceField(
        label='Cookies van derden toestaan?',
        required=True,
        widget=forms.RadioSelect(),
        choices=CHOICES,
    )

    def save(self, request):
        request.session['hide_modal'] = True
        request.session['analytical_cookies'] = self.cleaned_data['analytical_cookies'] == 'True'
        request.session['third_party_cookies'] = self.cleaned_data['third_party_cookies'] == 'True'
