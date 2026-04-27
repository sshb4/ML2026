from pathlib import Path
import pandas as pd


def main():
    root = Path(__file__).parent.resolve()
    csv = root / 'df_power.csv'
    print('Looking for dataset at:', csv)
    if not csv.exists():
        print('ERROR: df_power.csv not found in', root)
        return

    df = pd.read_csv(csv, low_memory=False)
    print('Loaded rows:', len(df), 'columns:', len(df.columns))
    print('\nColumns:', ', '.join(df.columns[:10]) + (', ...' if len(df.columns) > 10 else ''))
    print('\nSample rows:')
    print(df[['Season', 'Name', 'HR', 'prev_HR']].head().to_string(index=False))


if __name__ == '__main__':
    main()
