import hypothesis.strategies as st
from hypothesis import assume
from hypothesis import given

from rf_django_envconfig import get_bool
from rf_django_envconfig import get_list


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


@st.composite
def comma_separated_values(draw, elements=st.text()):
    xs = draw(st.lists(elements, average_size=10))
    return ','.join(xs)


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


@given(x=comma_separated_values())
def test_get_list(x):
    items = x.split(',')
    assert get_list({'test': x}, 'test') == items


@given(x=comma_separated_values())
def test_get_list_value_absent(x):
    assert get_list({}, 'test') == []


@given(x=comma_separated_values())
def test_get_list_value_absent_with_default(x):
    assert get_list({}, 'test', ['localhost', ]) == ['localhost', ]
