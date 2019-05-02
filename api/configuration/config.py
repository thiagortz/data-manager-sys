import os
from munch import Munch

_CONFIG = Munch()


def get_config():
    if not _CONFIG:
        try:
            _load_config()
        except KeyError as e:
            raise e

    return _CONFIG


def _load_config():
    env = os.environ

    _CONFIG.update(
        mode=env.get("MODE", True),
        host=env.get("HOST", "0.0.0.0"),
        port=env.get("PORT", 8000)
    )
