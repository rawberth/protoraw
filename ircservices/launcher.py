


from enrobie.clients.irc import IRCClient
from enrobie.clients.irc import IRCClientParams
from enrobie.execution.service import arguments
from enrobie.execution.service import operation
from enrobie.robie import Robie
from enrobie.robie import RobieConfig

from .plugin import ServicesPluginParams
from .plugin import ServicesPlugin



SERVER = ''    # address for IRC daemon
PORT = 6900
PASSWORD = ''  # connection password
MYFQDN = ''    # name for services server
ABOUT = 'Ohnope IRC Services'



def register_ircparams(
    config: RobieConfig,
) -> None:

    params = {
        'server': SERVER,
        'port': PORT,
        'operate': 'service',
        'realname': ABOUT,
        'password': PASSWORD,
        'servername': MYFQDN,
        'ssl_verify': False}

    source = {
        'enable': True,
        'client': params}

    config.register(
        'ircsvc',
        client=IRCClientParams,
        source=source)



def register_ircclient(
    robie: Robie,
) -> None:

    robie.register(
        'ircsvc',
        client=IRCClient)



def register_svcparams(
    config: RobieConfig,
) -> None:

    source = {'enable': True}

    config.register(
        'services',
        plugin=ServicesPluginParams,
        source=source)



def register_svcplugin(
    robie: Robie,
) -> None:

    robie.register(
        name='services',
        plugin=ServicesPlugin)



def execution() -> None:

    config = RobieConfig(
        arguments())

    register_ircparams(config)
    register_svcparams(config)

    config.logger.start()

    robie = Robie(config)

    register_ircclient(robie)
    register_svcplugin(robie)

    operation(robie)

    config.logger.stop()



if __name__ == '__main__':
    execution()
