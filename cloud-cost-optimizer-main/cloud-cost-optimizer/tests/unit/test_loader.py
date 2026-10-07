import pytest

from src.ingestion.exceptions import DataIngestionError
from src.ingestion.loader import BillingDataLoader


class TestBillingDataLoader:
    def test_load_valid_csv(self, sample_billing_file):
        loader = BillingDataLoader(sample_billing_file)
        data = loader.load_csv()
        assert data is not None
        assert len(data) > 0
        assert "resource_id" in data.columns
        assert "cost" in data.columns

    def test_missing_file_raises_error(self):
        loader = BillingDataLoader("nonexistent.csv")
        with pytest.raises(DataIngestionError):
            loader.load_csv()