from circus.commands.base import Command
from circus.exc import MessageError


class Listen(Command):
    """\
        Suscribe to a watcher event
        ===========================

        ZMQ
        ---

        At any moment you can suscribe to circus event. Circus provide a
        PUB/SUB feed on which any clients can suscribe. The suscriber
        endpoint URI is set in the circus.ini configuration file.

        Events are pubsub topics:

        Events are pubsub topics:

        - `watcher.<watchername>.reap`: when a process is reaped
        - `watcher.<watchername>.spawn`: when a process is spawned
        - `watcher.<watchername>.kill`: when a process is killed
        - `watcher.<watchername>.updated`: when watcher configuration
          is updated
        - `watcher.<watchername>.stop`: when a watcher is stopped
        - `watcher.<watchername>.start`: when a watcher is started

        All events messages are in a json.

        Command line
        ------------

        The client has been updated to provide a simple way to listen on the
        events::

            circusctl list [<topic>, ...]

        Example of result:
        ++++++++++++++++++

        ::

            $ circusctl listen tcp://127.0.0.1:5556
            watcher.refuge.spawn: {u'process_id': 6, u'process_pid': 72976,
                                   u'time': 1331681080.985104}
            watcher.refuge.spawn: {u'process_id': 7, u'process_pid': 72995,
                                   u'time': 1331681086.208542}
            watcher.refuge.spawn: {u'process_id': 8, u'process_pid': 73014,
                                   u'time': 1331681091.427005}
    """
    name = "listen"
    msg_type = "sub"

    def message(self, *args, **opts):
        if not args:
            return [""]
        return list(args)

    def execute(self, arbiter, args):
        raise MessageError("invalid message. use a pub/sub socket")
