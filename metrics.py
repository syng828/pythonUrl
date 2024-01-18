import enum

import prometheus_client


class Metrics(enum.Enum):
    url_count = ("url_count", "Number of URLs in the DB",
                 prometheus_client.Counter, ())
    query_time = ("query_time", "Time taken to execute the SQLite queries",
                  prometheus_client.Summary, ("query_type",))
    http_code = ("http_code", "Number of instances of each HTTP code",
                 prometheus_client.Counter, ("http_code",))

    def __init__(self, title, description, prometheus_type, labels=()):
        # we use the above default value for labels because it matches what's used
        # in the prometheus_client library's metrics constructor, see
        # https://github.com/prometheus/client_python/blob/fd4da6cde36a1c278070cf18b4b9f72956774b05/prometheus_client/metrics.py#L115
        self.title = title
        self.description = description
        self.prometheus_type = prometheus_type
        self.labels = labels


# A singleton class
class MetricsHandler:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call MetricsHandler.instance() instead')

    def init(self) -> None:
        for metric in Metrics:
            setattr(
                self,
                metric.title,
                metric.prometheus_type(
                    metric.title, metric.description, labelnames=metric.labels
                ),
            )

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.init(cls)
        return cls._instance