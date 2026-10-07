import os
import tempfile

import pandas as pd
import pytest


@pytest.fixture
def sample_billing_data():
    return pd.DataFrame(
        {
            "resource_id": ["i-001", "i-002", "i-003", "i-004"],
            "resource_type": ["EC2", "EC2", "EBS", "RDS"],
            "region": ["us-east-1", "us-east-1", "us-west-2", "us-east-1"],
            "usage_hours": [720, 720, 720, 720],
            "cost": [145.00, 89.00, 45.00, 200.00],
            "utilization": [0.023, 0.15, 0.0, 0.45],
        }
    )


@pytest.fixture
def sample_billing_file(sample_billing_data):
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    sample_billing_data.to_csv(path, index=False)
    yield path
    os.unlink(path)


@pytest.fixture
def high_utilization_data():
    return pd.DataFrame(
        {
            "resource_id": ["i-001", "i-002"],
            "resource_type": ["EC2", "EC2"],
            "region": ["us-east-1", "us-east-1"],
            "usage_hours": [720, 720],
            "cost": [145.00, 89.00],
            "utilization": [0.75, 0.85],
        }
    )