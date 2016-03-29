# coding=utf-8

START_URLS = "start_urls"
MAX_RETRY = "max_retry"
MAX_LEVEL = "max_level"
CHECK = "check"
FOLLOW = "follow"
DOWNLOADER_PLUGINS = "downloader_plugins"
SPIDER_PLUGINS = "spider_plugins"
SPIDER = "spider"

DEFAULT_CONFIG = {START_URLS: [],
                  MAX_RETRY: 3,
                  MAX_LEVEL: 0,
                  CHECK: [],
                  FOLLOW: {},
                  DOWNLOADER_PLUGINS: [],
                  SPIDER_PLUGINS: [],
                  SPIDER: None}


class TaskConfig:
    def __init__(self, **kw):
        self._config = dict(kw)

    def get(self, name):
        res = self._config.get(name)
        if not res:
            res = DEFAULT_CONFIG.get(name)
        return res

    def set(self, name, value):
        self._config[name] = value
