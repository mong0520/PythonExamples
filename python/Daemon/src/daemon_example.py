#!/usr/bin/env python
# sudo pip install python-daemon
#standard python libs
import logging
import time

#third party libs
from daemon import runner

class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/null'
        self.stderr_path = '/dev/null'
        # self.stdout_path = '/dev/tty'
        # self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/var/run/testdaemon.pid'
        self.pidfile_timeout = 5

    def run(self):
        while True:
            #Main code goes here ...
            #Note that logger level needs to be set to logging.DEBUG before this shows up in the logs
            logger.debug("Debug message")
            logger.info("Info message")
            logger.warn("Warning message")
            logger.error("Error message")
            time.sleep(10)

            
#def program_cleanup(signum, frame):
#   logger.debug('Shutdown')
    
app = App()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/testdaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)

# Override signal map, seems not a good way.
# daemon_runner.daemon_context.signal_map = {
#    signal.SIGTERM: program_cleanup,
#    signal.SIGHUP: program_cleanup
#}
#This ensures that the logger file handle does not get closed during daemonization
daemon_runner.daemon_context.files_preserve=[handler.stream]
try:
    daemon_runner.do_action()
except Exception as e:
    logger.error(e)
    
