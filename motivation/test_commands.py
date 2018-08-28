import functools

import pytest

from motivation import commands


def test_jm():
	res = commands.jm(None, None, "#inane", None, "")
	assert isinstance(res, str)


@pytest.mark.withoutresponses
def test_schneier():
	res = commands.schneier(None, None, "#inane", None, "foo")
	assert 'foo' in res


@pytest.fixture
def use_fact(responses):
	return functools.partial(
		responses.add,
		responses.GET,
		'https://www.schneierfacts.com/',
	)


def test_schneier_all_caps(use_fact):
	"At least one schneier fact features BRUCE SCHNEIER"
	use_fact('<p class="fact">How awesome is BRUCE SCHNEIER!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


def test_schneier_multi(use_fact):
	"At least one schneier fact features the phrase twice"
	use_fact(
		'<p class="fact">How awesome is Bruce '
		'Schneier? Bruce Schneier!</p>',
	)
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin? darwin!"


def test_schneier_no_space(use_fact):
	"At least one fact contains BRUCESCHNEIER"
	use_fact('<p class="fact">How awesome is BruceSchneier!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


def test_schneier_no_bruce(use_fact):
	"At least one fact contains only 'schneier'"
	use_fact('<p class="fact">How awesome is Schneier!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"


def test_schneier_no_schneier(use_fact):
	"At least one fact contains only 'bruce'"
	use_fact('<p class="fact">How awesome is Bruce!</p>')
	res = commands.schneier(None, None, "#inane", None, "darwin")
	assert res == "How awesome is darwin!"
