from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

from rippl.logging import slack as logger

User = get_user_model()


class RecaptchaRegistrationForm(RegistrationFormUniqueEmail):
    # comment this line out to enable registration in dev
    # TODO: make this more graceful
    captcha = ReCaptchaField(label="I'm a human")


class RecaptchaRegView(RegistrationView):
    form_class = RecaptchaRegistrationForm

    def register(self, form):
        username = form.cleaned_data.get(User.USERNAME_FIELD)
        logger.info("New user `{}` just registered".format(username))
        return super().register(form)
