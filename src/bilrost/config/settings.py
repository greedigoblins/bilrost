import pydantic_settings


class OTELExporterJaeger(pydantic_settings.BaseSettings):
    otel_exporter_jaeger_agent_host: str
    otel_exporter_jaeger_agent_port: int
    otel_exporter_jaeger_endpoint: str
    otel_exporter_jaeger_user: str
    otel_exporter_jaeger_password: str  # SECERT!
    otel_exporter_jaeger_timeout: int
    otel_exporter_jaeger_certificate: str
    otel_exporter_jaeger_agent_split_oversized_batches: bool
    otel_exporter_jaeger_grpc_insecure: bool


class OTELExporterZipkin(pydantic_settings.BaseSettings):
    otel_exporter_zipkin_endpoint: str
    otel_exporter_zipkin_timeout: int


class OTELExporterPrometheus(pydantic_settings.BaseSettings):
    otel_exporter_prometheus_host: str
    otel_exporter_prometheus_port: int


class OTELSDK(pydantic_settings.BaseSettings):
    otel_sdk_disabled: bool
    otel_log_level: bool
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


class OTELExportSelection(pydantic_settings.BaseSettings):
    otel_traces_exporter: str
    otel_metrics_exporter: str
    otel_logs_exporter: str


class OTELMetrics(pydantic_settings.BaseSettings):
    otel_metrics_exemplar_filter: str
    otel_metric_export_interval: int
    otel_metric_export_timeout: int
