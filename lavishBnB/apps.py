from django.apps import AppConfig


class LavishbnbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lavishBnB'

def ready(self):
    import lavishBnB.signals  # replace "lavishBnB" with the actual app name



