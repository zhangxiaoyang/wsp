# coding=utf-8

from wsp.utils.config import ensure_int

DEFAULT_KAFKA_CONSUMER_TIMEOUT_MS = 5000
DEFAULT_MONGO_DB = "wsp"
DEFAULT_MONGO_TASK_TBL = "task"
DEFAULT_MONGO_TASK_PROGRESS_TBL = "task_progress"
DEFAULT_MONGO_TASK_CONFIG_TBL = "task_config"
DEFAULT_TASK_CONFIG_FILE = "config.yaml"


class SystemConfig:

    def __init__(self, **kw):
        self.kafka_addr = kw.get("kafka_addr")
        self.mongo_addr = kw.get("mongo_addr")
        self.kafka_consumer_timeout_ms = ensure_int(kw.get("kafka_consumer_timeout_ms", DEFAULT_KAFKA_CONSUMER_TIMEOUT_MS))
        self.mongo_db = kw.get("mongo_db", DEFAULT_MONGO_DB)
        self.mongo_task_tbl = kw.get("mongo_task_tbl", DEFAULT_MONGO_TASK_TBL)
        self.mongo_task_progress_tbl = kw.get("mongo_task_progress_tbl", DEFAULT_MONGO_TASK_PROGRESS_TBL)
        self.mongo_task_config_tbl = kw.get("mongo_task_config_tbl", DEFAULT_MONGO_TASK_CONFIG_TBL)
        self.task_config_file = kw.get("task_config_file", DEFAULT_TASK_CONFIG_FILE)
        self.monitor_addr = kw.get("monitor_addr")
