from rf_django_envconfig import get_bool


def test_get_bool():
    false_values = [
        'False',
        'false',
        'Off',
        'off',
        '0',
        'No',
        'no',
        '',
    ]
    for value in false_values:
        env = {'test': value}
        assert not get_bool(env, 'test')
    assert get_bool({}, 'nosuchvar', default=True)
    assert not get_bool({}, 'nosuchvar')
    assert get_bool({'myvar': '1'}, 'myvar')
