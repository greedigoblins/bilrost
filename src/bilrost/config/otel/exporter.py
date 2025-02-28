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


class OTELExportSelection(pydantic_settings.BaseSettings):
    otel_traces_exporter: str
    otel_metrics_exporter: str
    otel_logs_exporter: str
