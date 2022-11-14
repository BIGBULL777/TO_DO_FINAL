from django.apps import AppConfig
# from suit.config import DjangoSuitConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

# class SuitConfig(DjangoSuitConfig):
#     layout = 'vertical'
