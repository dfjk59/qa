from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Post'))
