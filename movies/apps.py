from django.apps import AppConfig


# WARNINGS:
# movies.Movie: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
#         HINT: Configure the DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' setting in the settings.py or the MoviesConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'