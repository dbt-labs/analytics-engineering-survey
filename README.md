# Analytics Engineering Survey

## Clone
Prerequisities: `git`

See [here](gh-clone.md) for other cloning methods. 
```shell
git clone https://github.com/dbt-labs/analytics-engineering-survey.git
cd analytics-engineering-survey
```

## Install
Prerequisities: Python >= 3.5

The following will work for `zsh` and `bash`. See [here](create-virtual-environment.md) for other shells. 

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
```

## Run
```shell
dbt build
```

## Query

Launch a DuckDB command-line interface (CLI):
```shell
duckcli ae_survey.duckdb
```

Run a query at the prompt and exit:
```
select count(*) as count_responses from survey_results;
select * from survey_results where "Respondent ID" = 118190340290;
exit;
```

Alternatively, use a single-liner to perform the query:
```shell
duckcli ae_survey.duckdb -e 'select * from survey_results where "Respondent ID" = 118190340290'
```
or:
```shell
echo 'select * from survey_results where "Respondent ID" = 118190340290' | duckcli ae_survey.duckdb
```
