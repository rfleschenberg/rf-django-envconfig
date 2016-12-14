from hypothesis import given, assume
import hypothesis.strategies as st

from rf_django_envconfig import get_bool


FALSE_VALUES = [
    'False',
    'false',
    'Off',
    'off',
    '0',
    'No',
    'no',
    '',
]


@given(x=st.text())
def test_get_bool_true(x):
    assume(x not in FALSE_VALUES)
    env = {'test': x}
    assert get_bool(env, 'test')


@given(x=st.text())
def test_get_bool_false(x):
    assume(x in FALSE_VALUES)
    env = {'test': x}
    assert not get_bool(env, 'test')


@given(x=st.text())
def test_get_bool_default_true_value_absent(x):
    assert get_bool({}, 'test', default=True)


@given(x=st.text())
def test_get_bool_default_false_value_absent(x):
    assert not get_bool({}, 'test',  default=False)


@given(x=st.text())
def test_get_bool_default_true_value_present(x):
    assume(x in FALSE_VALUES)
    env = {'test': x}
    assert not get_bool(env, 'test',  default=True)


@given(x=st.text())
def test_get_bool_default_false_value_present(x):
    assume(x not in FALSE_VALUES)
    env = {'test': x}
    assert get_bool(env, 'test',  default=False)
