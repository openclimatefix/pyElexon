from pyelexon.balancing.settlement.main import get_system_prices


def test_get_balancing_settlement_system_prices():

    df = get_system_prices("2024-04-01")

    assert len(df) == 48
    assert "settlementDate" in df.columns
    assert "settlementPeriod" in df.columns
    assert "startTime" in df.columns
    assert "createdDateTime" in df.columns
    assert "systemSellPrice" in df.columns
    assert "netImbalanceVolume" in df.columns

