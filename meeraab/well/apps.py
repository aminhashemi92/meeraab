from django.apps import AppConfig


class WellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'well'
    verbose_name = "حساب‌ها"

    def ready(self):
        import well.signals
