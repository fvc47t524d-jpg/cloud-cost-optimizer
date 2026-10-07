"""Loads and validates cloud billing data from various file formats."""

import pandas as pd

from .exceptions import DataIngestionError, SchemaValidationError


class BillingDataLoader:
    """Loads and validates cloud billing data from CSV and JSON files."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None
        self.required_fields = [
            "resource_id",
            "resource_type",
            "region",
            "usage_hours",
            "cost",
        ]

    def load_csv(self) -> pd.DataFrame:
        """Load billing data from a CSV file with validation."""
        try:
            self.data = pd.read_csv(self.file_path)
            self._validate_schema()
            self._validate_data_types()
            return self.data
        except FileNotFoundError:
            raise DataIngestionError(f"File not found: {self.file_path}")
        except pd.errors.EmptyDataError:
            raise DataIngestionError("File is empty or corrupted")

    def load_json(self) -> pd.DataFrame:
        """Load billing data from a JSON file with validation."""
        try:
            self.data = pd.read_json(self.file_path)
            self._validate_schema()
            self._validate_data_types()
            return self.data
        except FileNotFoundError:
            raise DataIngestionError(f"File not found: {self.file_path}")

    def _validate_schema(self) -> None:
        missing = [f for f in self.required_fields if f not in self.data.columns]
        if missing:
            raise SchemaValidationError(f"Missing required fields: {missing}")

    def _validate_data_types(self) -> None:
        for field in ["usage_hours", "cost"]:
            if field in self.data.columns:
                if not pd.api.types.is_numeric_dtype(self.data[field]):
                    self.data[field] = pd.to_numeric(
                        self.data[field], errors="coerce"
                    ).fillna(0)