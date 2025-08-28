# Refactor Demo - Clean Task

## Description
This script refactors the data cleaning task into a CLI-callable function.

## How to Run
- Install dependencies: `pip install -r ../requirements.txt`
- Execute: `python clean_task.py --input /path/to/train.csv --output /path/to/prices_clean.json`
- Logs: Outputs start/end and file write status to console.

## Notes
Assumes CSV input with numeric columns; fills NA with median values.
