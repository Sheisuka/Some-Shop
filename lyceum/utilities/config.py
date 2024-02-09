from os import environ


def get_env_var(var_name):
    var = environ.get(var_name)
    if var is not None:
        return var
    return ""
