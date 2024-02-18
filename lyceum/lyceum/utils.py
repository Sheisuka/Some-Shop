import os


def get_bool_from_env(key, default="y"):
    val = os.environ.get(key)
    if not val:
        val = default
        
    return val.lower() in ("yes", "true", "1", "y", "t")