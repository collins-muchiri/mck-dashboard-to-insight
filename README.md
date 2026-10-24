# mck-dashboard-to-insight

Portfolio artifact 3 of 3: a dashboard-to-insight write-up. It takes one finding from a programme dashboard, shows the analysis that confirms it, and states the programme decision it implies.

ALL DATA IN THIS REPOSITORY IS SYNTHETIC. It is labelled synthetic on every figure and in every file. No client, programme or beneficiary data is present.

## The finding

In the synthetic programme dashboard at figures/dash_page3_data_quality.png, two of eight counties, Turkana and Garissa, report 52 to 81 per cent of expected records per month while the other six report 88 to 100 per cent. GPS point completeness sits at 82.3 per cent against a 95 per cent standard, concentrated in the same two counties. Duplicate national identifier is the largest single validation failure at 147 records.

## The confirming analysis

1. Coverage by county and month shows the gap is persistent across all seven months, not a single bad upload, which rules out a transient pipeline fault.
2. The gap correlates with submission lag: the same partners reporting late are the partners reporting thin, which points at field capacity rather than at the data system.
3. Completeness of mandatory fields is above 95 per cent for records that do arrive, so the problem is missing records, not malformed ones. Missingness and malformedness require different fixes and are often confused.

## The decision it implies

Do not publish a single aggregate beneficiary count for the programme. Report Turkana and Garissa separately with the coverage gap disclosed, and suspend their inclusion in the regional aggregate until coverage exceeds 90 per cent for two consecutive months. An average that silently absorbs a 40 per cent reporting gap is a number that will be quoted back at the programme in a donor meeting.

## Figures

- figures/dash_page1_director_view.png, the director view
- figures/dash_page2_programme_view.png, trends and disaggregation
- figures/dash_page3_data_quality.png, the data quality view this note reads from

## Licence

MIT. See LICENSE.
