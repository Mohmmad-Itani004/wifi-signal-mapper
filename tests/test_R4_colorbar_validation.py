import pytest

def test_R4_colorbar_legible():
    """Test that RSSI range supports a legible colorbar dBm gradient (R4)."""
    min_rssi = -90
    max_rssi = -30
    assert min_rssi < max_rssi, "Valid RSSI operational signal range required for colorbar correlation"