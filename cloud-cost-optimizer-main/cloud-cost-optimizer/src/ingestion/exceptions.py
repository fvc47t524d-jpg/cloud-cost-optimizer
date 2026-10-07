"""Custom exceptions for the data ingestion module."""


class DataIngestionError(Exception):
    """Raised when data ingestion fails."""
    pass


class SchemaValidationError(DataIngestionError):
    """Raised when schema validation fails."""
    pass