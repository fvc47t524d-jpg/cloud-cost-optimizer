"""Idle resource detection algorithm."""

import pandas as pd


class IdleResourceDetector:
    """Identifies resources with utilization below a configurable threshold."""

    def __init__(self, utilization_threshold: float = 0.05):
        self.threshold = utilization_threshold
        self.detection_results = []

    def detect_idle_resources(self, df: pd.DataFrame) -> list:
        if df.empty:
            return []

        idle_resources = []
        for resource_id, group in df.groupby("resource_id"):
            avg_utilization = group["utilization"].mean()
            if avg_utilization < self.threshold:
                monthly_cost = group["cost"].sum()
                potential_savings = monthly_cost * 0.9
                idle_resources.append(
                    {
                        "resource_id": resource_id,
                        "resource_type": group["resource_type"].iloc[0],
                        "avg_utilization": round(avg_utilization * 100, 2),
                        "monthly_cost": round(monthly_cost, 2),
                        "potential_savings": round(potential_savings, 2),
                        "priority": self._calculate_priority(monthly_cost),
                        "explanation": self._generate_explanation(
                            avg_utilization, monthly_cost
                        ),
                        "confidence": "HIGH" if avg_utilization < 0.02 else "MEDIUM",
                    }
                )

        self.detection_results = idle_resources
        return idle_resources

    def _calculate_priority(self, cost: float) -> str:
        if cost > 100:
            return "HIGH"
        if cost > 50:
            return "MEDIUM"
        return "LOW"

    def _generate_explanation(self, utilization: float, cost: float) -> str:
        return (
            f"This resource has maintained average utilization of "
            f"{utilization * 100:.1f}% over the analysis period. "
            f"Monthly cost is ${cost:.2f}. Consider terminating if not "
            f"needed or downsizing to reduce costs."
        )