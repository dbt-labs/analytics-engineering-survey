import pandas as pd


def model(dbt, _):
    dbt.config(
        materialized="table",
    )
    relation = dbt.ref("survey_results")

    # Convert the relation to a Pandas DataFrame
    pdf = relation.to_df()

    # Generate descriptive statistics of each question of the survey results
    df = pdf.describe(include="all") #.transpose()

    # Include the statistic name in the tabular output
    df.reset_index(inplace=True)
    df = df.rename(columns={"index": "statistic"})

    return df
