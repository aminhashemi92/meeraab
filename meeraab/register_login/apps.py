from django.apps import AppConfig


class RegisterLoginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'register_login'

    verbose_name = "حساب‌های کاربری و نقش‌ها"

    def ready(self):
        import register_login.signals
