import mock

# mock the pmxbot imports
pmxbot = mock.MagicMock()
pmxbot.core = mock.MagicMock(command=mock.Mock(return_value=lambda func:func))
pmxbot.karma = mock.MagicMock()

def pytest_configure(config):

	patcher = mock.patch.dict('sys.modules', {
		'pmxbot': pmxbot,
		'pmxbot.core': pmxbot.core,
		'pmxbot.karma': pmxbot.karma,
	})
	patcher.__enter__()
