__version__ = "0.1.0"


def get_bool(env, name, default=False):
    """Get a boolean value from the environment

    If the value is not set in the environment, return ``True`` if ``default``
    evaluates to ``True``, otherwise return ``False``.

    The following values are considered ``False``:

        * ``'False'``
        * ``'false'``
        * ``'Off'``
        * ``'off'``
        * ``'0'``
        * ``'No'``
        * ``'no'``
        * ``''``

    Any other value is considered ``True``.
    """
    if name not in env:
        return bool(default)
    value = env[name]
    if value in ['False', 'false', 'Off', 'off', '0', 'No', 'no', '']:
        return False
    return True


def get_list(env, name, default=None):
    """Get a list from the environment

    The input is assumed to be a comma-separated list of strings.

    If ``name`` is not present in the environment, return ``default``. Note
    that ``default`` is returned as-is, so you should usually specify it as a
    list::

        ALLOWED_HOSTS = get_list(os.environ, 'ALLOWED_HOSTS', ['localhost', ])
    """
    if default is None:
        default = []
    if name not in env:
        return default
    return env[name].split(',')
