import enum
from typing import Any

import pydantic
import pydantic_settings

_OTEL_COMPRESSION_MAP = {
    "gzip": "grpc.Compression.Gzip",
    "deflate": "grpc.Compression.Deflate",
    "none": "grpc.Compression.NoCompression",
}


class CompressionEnum(enum.StrEnum):
    GZIP = enum.auto()
    DEFLATE = enum.auto()
    NONE = enum.auto()


class TemporalityPreferenceEnum(enum.StrEnum):
    CUMULATIVE = enum.auto()
    DELTA = enum.auto()
    LOWMEMORY = enum.auto()


class HistogramAggregationEnum(enum.StrEnum):
    EXPLICIT_BUCKET_HISTOGRAM = enum.auto()
    BASE2_EXPONENTIAL_BUCKET_HISTOGRAM = enum.auto()


OTELExporterConfigrationOptions = {
    "endpoint": (
        str,
        pydantic.Field(
            "http://localhost:4317",
            description="Endpoint must be a valid URL host, and MAY contain a scheme (http or https), port and path.",
        ),
    ),
    "protocol": (
        str,
        pydantic.Field("http/protobuf", description="Transport protocol."),
    ),
    "certificate": (
        str,
        pydantic.Field(
            description=(
                "Path to the certificate file for TLS credentials of gRPC client. "
                "Should only be used for a secure connection."
            )
        ),
    ),
    "compression": (
        CompressionEnum,
        pydantic.Field(description="Specifies a gRPC compression method."),
    ),
    "timeout": (
        int,
        pydantic.Field(
            10,
            description="Maximum time the OTLP exporter will wait for each batch export.",
            ge=0,
        ),
    ),
    "insecure": (
        bool,
        pydantic.Field(
            False,
            description=(
                "Whether to enable client transport security for gRPC requests. "
                "A scheme of https takes precendence over this configuration setting."
            ),
        ),
    ),
    "headers": (
        str,
        pydantic.Field(
            description="Contains key-value pairs to be used as headers associated with the gRPC or HTTP requests."
        ),
    ),
    "client_key": (
        str,
        pydantic.Field(
            description="Path to the client private key to use in mTLS communication in PEM format"
        ),
    ),
    "client_certificate": (
        str,
        pydantic.Field(
            description=(
                "Path to the client certificate/chain trust for client's private key to use in mTLS "
                "communication in PEM format."
            )
        ),
    ),
}


def _exporter_otlp_factory(
    model_name: str,
    prefix: str,
    additional_fields: dict[str, tuple[type, Any]] | None = None,
) -> type[pydantic_settings.BaseSettings]:
    """
    :param model_name:
    :param prefix:
    :param additional_fields: Dictionary of fields that allows the user to overwrite the defaults and add new fields
    """
    additional_fields = {} if additional_fields is None else additional_fields
    fields_dict = OTELExporterConfigrationOptions | additional_fields
    field_definitions = {f"{prefix}_{key}": defn for key, defn in fields_dict.items()}
    return pydantic.create_model(
        model_name,
        __config__=None,
        __cls_kwargs__=None,
        __doc__=None,
        __module__=__name__,
        __validators__=None,
        __base__=pydantic_settings.BaseSettings,
        **field_definitions,
    )


OTELExporterOTLP = _exporter_otlp_factory(
    "OTELExporterOTLP",
    "otel_exporter_otlp",
    additional_fields={
        "metrics_temporality_preference": (
            TemporalityPreferenceEnum,
            pydantic.Field(
                description="Default aggregation temporality policy to use on the basis of instrument kind."
            ),
        ),
        "metrics_default_histogram_aggregation": (
            HistogramAggregationEnum,
            pydantic.Field(
                description="Default aggregation to use for histogram instruments."
            ),
        ),
    },
)

OTELExporterOTLPMetrics = _exporter_otlp_factory(
    "OTELExporterOTLPMetrics", "otel_exporter_otlp_metrics"
)

OTELExporterOTLPLogs = _exporter_otlp_factory(
    "OTELExporterOTLPLogs", "otel_exporter_otlp_logs"
)
OTELExporterOTLPTraces = _exporter_otlp_factory(
    "OTELExporterOTLPTraces", "otel_exporter_otlp_traces"
)
