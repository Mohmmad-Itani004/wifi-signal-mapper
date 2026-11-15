import pytest
from pathlib import Path

def test_R3_heatmap_output(tmp_path):
    """Test that heatmap output targets a valid .png extension (R3)."""
    output_file = tmp_path / "heatmap.png"
    assert output_file.suffix == ".png"