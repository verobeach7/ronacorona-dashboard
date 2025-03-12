import pandas as pd


def make_global_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = (
        df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
        .sum()
        .reset_index(name=condition)
    )
    df = df.rename(columns={"index": "date"})
    return df


daily_df = pd.read_csv("data/daily_report.csv")

totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)
totals_df = totals_df.rename(columns={"index": "condition"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


conditions = ["confirmed", "deaths", "recovered"]

final_df = None

for condition in conditions:
    condition_df = make_global_df(condition)
    # 처음에만 실행됨
    if final_df is None:
        final_df = condition_df
    else:
        # .merge()를 사용하면 공통키를 기준으로 병합해줌
        final_df = final_df.merge(condition_df)
