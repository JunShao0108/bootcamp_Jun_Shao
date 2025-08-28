import argparse
import json
import logging
import sys
from pathlib import Path
from datetime import datetime

def clean_task(input_path: str, output_path: str) -> None:
    '''Clean raw data by handling missing values and saving to JSON.'''
    logging.info('[clean_task] start')
    df = pd.read_csv(input_path)
    # Simple cleaning: fill NA with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col].fillna(df[col].median(), inplace=True)
    result = df.to_dict(orient='records')
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(result, indent=2))
    logging.info('[clean_task] wrote %s', output_path)

def main(argv=None):
    parser = argparse.ArgumentParser(description='Clean raw housing data')
    parser.add_argument('--input', required=True, help='Input CSV file path')
    parser.add_argument('--output', required=True, help='Output JSON file path')
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
    clean_task(args.input, args.output)

if __name__ == '__main__':
    main(['--input', '/Users/junshao/bootcamp_Jun_Shao/homework/hw15/data/raw/train.csv', 
          '--output', '/Users/junshao/bootcamp_Jun_Shao/homework/hw15/data/processed/prices_clean.json'])
