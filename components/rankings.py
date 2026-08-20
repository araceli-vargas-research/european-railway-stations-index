import streamlit as st

def render_rankings_table(df):
    display = df.sort_values(
        ["total_score", "station"], ascending=[False, True]
    )[[
        "rank_2026", "country", "city", "station", "total_score",
        "passenger_volume_latest", "delay_percent_2026", "wait_minutes_2026"
    ]].rename(columns={
        "rank_2026": "Rank",
        "country": "Country",
        "city": "City",
        "station": "Station",
        "total_score": "Score",
        "passenger_volume_latest": "Passenger volume (m)",
        "delay_percent_2026": "Delayed trains (%)",
        "wait_minutes_2026": "Avg. wait (min)",
    })

    st.dataframe(display, hide_index=True, use_container_width=True, height=460)
