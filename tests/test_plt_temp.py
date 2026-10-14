
from plt_temp import make_temperature_df


def test_columns():
    df = make_temperature_df(
        ["2026-10-14T02:00", "2026-10-14T01:00"],
        [5.0, 4.0],
    )
    assert list(df.columns) == ["time", "temperature_c"]


def test_row_count():
    df = make_temperature_df(
        ["2026-10-14T01:00", "2026-10-14T02:00"],
        [4.0, 5.0],
    )
    assert len(df) == 2


def test_sorted_by_time():
    df = make_temperature_df(
        ["2026-10-14T02:00", "2026-10-14T01:00"],
        [5.0, 4.0],
    )
    assert df["time"].is_monotonic_increasing


def test_temperatures_preserved_after_sort():
    df = make_temperature_df(
        ["2026-10-14T02:00", "2026-10-14T01:00"],
        [5.0, 4.0],
    )
    assert df["temperature_c"].tolist() == [4.0, 5.0]