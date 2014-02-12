from pmxbot.core import command
from pmxbot.karma import Karma

@command('pm', aliases=('piratemotivate',), doc='Arggh matey')
def pm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel

    if nick == 'Dusty':
        # Dusty thinks double adjectives are more piratey.
        return "Arrggh ye be doin' great, grand work, %s!" % rcpt
    return "Arrggh ye be doin' good work, %s!" % rcpt


@command('lm', aliases=('latinmotivate',), doc='Rico Suave')
def lm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return '¡Estás haciendo un buen trabajo, %s!' % rcpt

@command('fm', aliases=('frenchmotivate',), doc='Michel puts on the moves')
def fm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return 'Vous bossez bien, %s!' % rcpt

@command('jm', aliases=('japanesemotivate',), doc='')
def jm(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel

    hon_romaji = ' san'
    hon_ja = ' さん'

    # Use correct honorific.
    if rcpt.lower().startswith('michel'):
        hon_romaji = ' sensei'
        hon_ja = ' 先生'

    elif rcpt == channel:
        hon_romaji = ''
        hon_ja = ''

    emoji = '(^_−)−☆'

    # reference the vars to avoid linter warnings
    emoji, hon_romaji, hon_ja

    return (
        '{rcpt}{hon_ja}, あなたわよくやっています! '
        '({rcpt}{hon_romaji}, anata wa yoku yatte '
        'imasu!)  -  {emoji}'.format(**vars())
    )

@command('danke', aliases=('dankeschoen','ds','gm','germanmotivate'), doc='Danke schön!')
def danke(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        change = -1 if 'istvan' in rest else 1 # istvan strives for negative karma
        Karma.store.change(rest, change)
        rcpt = rest
    else:
        rcpt = channel
    extra = ', Du kölsche Jung' if rcpt == 'cperry' else ''
    return 'Danke schön, {rcpt}! Danke schön{extra}!'.format(
        rcpt=rcpt, extra=extra)

@command('esperantomotivate', aliases=('em',), doc='Esperanto motivate')
def em(client, event, channel, nick, rest):
    if rest:
        rest = rest.strip()
        Karma.store.change(rest, 2)
        rcpt = rest
    else:
        rcpt = channel
    return 'Vi faras bonan laboron, {rcpt}!'.format(rcpt=rcpt)
