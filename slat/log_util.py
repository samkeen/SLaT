import logging
import os


class LogUtil:

    @staticmethod
    def init_logger(env_var_name: str = 'LOG_LEVEL', default_level: str = 'INFO') -> logging.Logger:
        """

        :param env_var_name: Looks for log level set at this ENV var name
        :type env_var_name: str
        :param default_level: Run this level if env_var_name not found
        :type default_level: str
        :return:
        :rtype: Logging.Logger
        """
        log_level = os.getenv(env_var_name, default_level)
        logger = logging.getLogger()
        logger.setLevel(log_level)
        return logger
