from os import environ

from django.core.exceptions import ImproperlyConfigured


def get_env_var(var_name):
    var = environ.get(var_name)
    if var != None:
        return var
    return ""