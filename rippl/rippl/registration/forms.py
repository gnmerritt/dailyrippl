from captcha.fields import ReCaptchaField
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationForm


class RecaptchaRegistrationForm(RegistrationForm):
    captcha = ReCaptchaField(label="I'm a human")


class RecaptchaRegView(RegistrationView):
    form_class = RecaptchaRegistrationForm
