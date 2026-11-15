import pytest
from pathlib import Path
import pandas as pd

def test_R2_spatial_interpolation():
    """Test that spatial data has sufficient variance for 2D interpolation (R2)."""
    csv_path = Path("data/measurements.csv")
    df = pd.read_csv(csv_path)
    assert df['rssi'].nunique() > 1, "RSSI values must vary for meaningful 2D spatial interpolation"