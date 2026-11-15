import pytest
from pathlib import Path
import pandas as pd

def test_R1_R5_valid_csv_loading():
    """Test that the CSV loads at least 20 valid points with correct columns (R1, R5)."""
    csv_path = Path("data/measurements.csv")
    assert csv_path.exists(), "measurements.csv must exist in data/"
    df = pd.read_csv(csv_path)
    assert len(df) >= 20, "Dataset must contain at least 20 spatial points (R5)"
    assert {"x", "y", "rssi"}.issubset(df.columns), "CSV must contain x, y, and rssi columns"