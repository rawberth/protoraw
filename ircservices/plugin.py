


from encommon.times import Time

from enrobie.robie.childs import RobiePlugin
from enrobie.robie.params import RobiePluginParams
from enrobie.robie.threads import RobieThread

from .common import SERVICES



class ServicesPluginParams(RobiePluginParams, extra='forbid'):
    """
    Process and validate the Robie configuration parameters.
    """



class ServicesPlugin(RobiePlugin):
    """
    Integrate with the Robie routine and perform operations.

    .. note::
       This plugin operates the related IRC network services.

    :param robie: Primary class instance for Chatting Robie.
    """


    def validate(
        self,
    ) -> None:
        """
        Perform advanced validation on the parameters provided.
        """

        # Nothing to do for plugin


    def operate(
        self,
        thread: RobieThread,
    ) -> None:
        """
        Perform the operation related to Homie service threads.

        :param thread: Child class instance for Chatting Robie.
        """

        robie = thread.robie
        mqueue = thread.mqueue
        childs = robie.childs
        clients = childs.clients


        def _register(
            nick: str,
            uid: str,
            about: str,
        ) -> None:

            epoch = Time().spoch

            _client = client.client

            serverid = (
                client.params
                .client.serverid)

            uid = serverid + uid

            _client.socket_send(
                f':{serverid} UID'
                f' {nick} 0 {epoch}'
                f' service {sname}'
                f' {uid} 0 +Sio'
                f' {sname} {sname}'
                f' * :{about}')


        while not mqueue.empty:

            mitem = mqueue.get()

            client = clients[
                mitem.client]

            event = (
                mitem.event
                .original)

            sname = (
                client.params
                .client
                .servername)

            if event[:8] == 'NETINFO ':

                for service in SERVICES:
                    _register(*service)
