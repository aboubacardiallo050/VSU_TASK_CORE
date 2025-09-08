import logging
import os

from dotenv import load_dotenv

from vsu_task_core.common.base import Applier

logger = logging.getLogger(__name__)


class Initializer(Applier):

    def apply(self, env_file_path_in: str) -> None:
        if os.path.exists(env_file_path_in):
            load_dotenv(env_file_path_in)
