import logging, coloredlogs

class Logger:
    def __init__(self, name: str, init_message: bool = False):
        self._logger = logging.getLogger(name)

        coloredlogs.install(logger=self._logger,
                            level="DEBUG")

        # all logger methods
        self.debug = self._logger.debug
        self.info = self._logger.info
        self.warning = self._logger.warning
        self.error = self._logger.error
        self.critical = self._logger.critical

        if init_message:
            self._logger.debug("Logger initialized")
