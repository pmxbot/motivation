import mock

# mock the pmxbot imports
class pmxbot_mod:
	config = {}

class core_mod:
	def command(*args, **kwargs):
		return lambda func: func

class karma_mod:
	class Karma:
		class store:
			def change(*args, **kwargs):
				pass

def pytest_configure(config):

	patcher = mock.patch.dict('sys.modules', {
		'pmxbot': pmxbot_mod,
		'pmxbot.core': core_mod,
		'pmxbot.karma': karma_mod,
	})
	patcher.__enter__()
