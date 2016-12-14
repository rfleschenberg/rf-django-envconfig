__version__ = "0.1.0"


def get_bool(env, name, default=False):
    """Get a boolean value from the environment

    If the value is not set in the environment, return ``True`` if ``default``
    evaluates to ``True``, otherwise return ``False``.

    The following values are considered ``False``:

        * 'False'
        * 'false'
        * 'Off'
        * 'off'
        * '0'
        * 'No'
        * 'no'
        * ''

    Any other value is considered ``True``.
    """
    if name not in env:
        return bool(default)
    value = env[name]
    if value in ['False', 'false', 'Off', 'off', '0', 'No', 'no', '']:
        return False
    return True
