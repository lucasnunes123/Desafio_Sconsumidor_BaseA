from django.apps import AppConfig


class BaseAAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_a_app'
