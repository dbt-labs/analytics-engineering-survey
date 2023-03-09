In late 2022, dbt Labs ran the first State of Analytics Engineering survey. Alongside the [main report](https://www.getdbt.com/state-of-analytics-engineering-2023/), we have released the raw data from 567 respondents for the community to explore. 

If you find something interesting, please share it in [Show and Tell on the Community Forum](https://discourse.getdbt.com/c/show-and-tell/22), or [#i-made-this](https://getdbt.slack.com/archives/C01NH3F2E05) in Slack.

## Data available
This repo contains two seed files:
`ae_survey_responses_2022.csv`: The responses from all survey participants, with one row per response and one column per possible answer. 

Single response answers such as *"Which of the following best describes how you distribute work within your data team?"* have a single column (e.g. `how_do_you_distribute_data_team_work`) containing the response. If the option to specify an alternative answer was available, there will be a second column (e.g. `how_do_you_distribute_data_team_work_other_free_text`). All free text responses have been replaced by a `1` to indicate that a response was given but redacted to avoid de-anonymisation risk. 

Multichoice answers are split across multiple columns. For example, in the multichoice question *"Which of the following best describes how you spend most of your time? Select all that apply."*, there are six columns with names such as `time_spent_multiselect_platform` and `time_spent_multiselect_datasets`, reflecting the answers *"Build / maintain platforms for hosting, moving, accessing data"* and *"Build / maintain data sets to ease analysis"* respectively.

All columns in this seed have accepted values tests (defined in `ae_survey_responses_2022.yml`). 

`ae_survey_questions_2022.csv`: The questions asked of the respondents. `short_column_name` maps to the columns in the responses seed, while `original_question` maps to the full question asked.

## Using the data

You can interact with the data in one of two ways: 
- Install this repo as a dbt package into an existing project;
- Download the data locally to query directly with DuckDB.

## To install as a dbt Package
To install a [git package](https://docs.getdbt.com/docs/build/packages#git-packages), add the following to your `packages.yml` file:
```yaml
packages:
  - git: "https://github.com/dbt-labs/analytics-engineering-survey.git"
    revision: main
```

Run `dbt deps`, then `dbt seed`. 

## To download for local use

### Clone
Prerequisities: `git`

See [here](gh-clone.md) for other cloning methods. 
```shell
git clone https://github.com/dbt-labs/analytics-engineering-survey.git
cd analytics-engineering-survey
```

### Install
Prerequisities: Python >= 3.5

The following will work for `zsh` and `bash`. See [here](create-virtual-environment.md) for other shells. 

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
```

### Run
```shell
dbt build
```

### Query

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
