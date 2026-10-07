import pandas as pd

from src.analysis.idle_detector import IdleResourceDetector


class TestIdleResourceDetector:
    def test_detect_idle_below_threshold(self, sample_billing_data):
        detector = IdleResourceDetector(utilization_threshold=0.05)
        results = detector.detect_idle_resources(sample_billing_data)
        assert len(results) == 2
        for rec in results:
            assert rec["avg_utilization"] < 5.0

    def test_no_detection_above_threshold(self, high_utilization_data):
        detector = IdleResourceDetector(utilization_threshold=0.05)
        results = detector.detect_idle_resources(high_utilization_data)
        assert len(results) == 0

    def test_priority_calculation(self):
        detector = IdleResourceDetector()
        assert detector._calculate_priority(150.00) == "HIGH"
        assert detector._calculate_priority(75.00) == "MEDIUM"
        assert detector._calculate_priority(25.00) == "LOW"

    def test_empty_dataframe_handling(self):
        detector = IdleResourceDetector()
        results = detector.detect_idle_resources(pd.DataFrame())
        assert results == []