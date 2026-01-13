def calculate_kpis(df):
    latest = df.iloc[-1]

    kpis = {
        "latest_exposure": latest["exposure"],
        "latest_default_rate": latest["default_rate"],
        "exposure_growth_pct": (
            (df.iloc[-1]["exposure"] - df.iloc[0]["exposure"])
            / df.iloc[0]["exposure"]
        ) * 100
    }

    return kpis
