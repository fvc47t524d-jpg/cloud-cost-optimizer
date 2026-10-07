"""Cleans and transforms raw billing data for analysis."""

import pandas as pd


class DataProcessor:
    """Cleans and normalizes raw billing data."""

    def __init__(self):
        self.processing_log = []

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_count = len(df)

        df["cost"] = df["cost"].fillna(0)
        df["usage_hours"] = df["usage_hours"].fillna(0)

        if "timestamp" in df.columns:
            df = df.drop_duplicates(subset=["resource_id", "timestamp"])

        df["cost_per_hour"] = df.apply(
            lambda x: x["cost"] / x["usage_hours"] if x["usage_hours"] > 0 else 0,
            axis=1,
        )

        self.processing_log.append(
            {
                "initial_records": initial_count,
                "final_records": len(df),
                "duplicates_removed": initial_count - len(df),
            }
        )
        return df