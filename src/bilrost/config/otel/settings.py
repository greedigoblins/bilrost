import enum

import pydantic_settings


class LogLevelEnum(enum.Enum):
    """Custom Enum generation class to set log levels

    Allows a mapping from severity values to log levels as part of the enum definition
    """

    def __new__(cls, name: str, lb: int, ub: int, description: str) -> "LogLevelEnum":
        self: LogLevelEnum = object.__new__(cls)
        self._value_ = name
        for v in range(lb, ub + 1):
            self._add_value_alias_(v)  # type: ignore
        return self

    def __init__(self, name: str, lb: int, ub: int, description: str) -> None:
        self.description = description


class LogLevel(LogLevelEnum):
    TRACE = "trace", 1, 4, "Fine-grained debugging event."
    DEBUG = "debug", 5, 8, "Debugging event."
    INFO = "info", 9, 12, "Informational event. Indicates that an event happened."
    WARN = (
        "warn",
        13,
        16,
        "Warning event. Not an error but is likely more important than an informational event.",
    )
    ERROR = "error", 17, 20, "Error event. Something went wrong."
    FATAL = "fatal", 21, 24, "Fatal error event such as an application or system crash."


class OTELSDK(pydantic_settings.BaseSettings):
    otel_sdk_disabled: bool = False
    otel_log_level: LogLevel = LogLevel.INFO
    otel_resource_attributes: bool
    otel_service_name: str
    otel_propagators: str
    otel_traces_sampler: str
    otel_traces_sampler_arg: str


class OTELBatchSpanProcessor(pydantic_settings.BaseSettings):
    otel_bsp_schedule_delay: int
    otel_bsp_export_timeout: int
    otel_bsp_max_queue_size: int
    otel_bsp_max_export_batch_size: int


class OTELBatchLogProcessor(pydantic_settings.BaseSettings):
    otel_blrp_schedule_delay: int
    otel_blrp_export_timeout: int
    otel_blrp_max_queue_size: int
    otel_blrp_max_export_batch_size: int


class OTELAttributeLimits(pydantic_settings.BaseSettings):
    otel_attribute_value_length_limit: int
    otel_attribute_count_limit: int


class OTELSpanLimits(pydantic_settings.BaseSettings):
    otel_span_attribute_value_length_limit: int
    otel_span_attribute_count_limit: int
    otel_span_event_count_limit: int
    otel_span_link_count_limit: int
    otel_event_attribute_count_limit: int
    otel_link_attribute_count_limit: int


class OTELLogRecordLimits(pydantic_settings.BaseSettings):
    otel_logrecord_attribute_value_length_limit: int
    otel_logrecord_attribute_count_limit: int


class OTELMetrics(pydantic_settings.BaseSettings):
    otel_metrics_exemplar_filter: str
    otel_metric_export_interval: int
    otel_metric_export_timeout: int
