import argparse
from pathlib import Path
import pandas as pd
from pybaseball import batting_stats


def build_df(start=2016, end=2025, qual=1):
	df = batting_stats(start, end, qual=qual)
	power_hitters = df[df['HR'] >= 1]['Name'].unique()
	df_power = df[df['Name'].isin(power_hitters)]
	df_power = df_power.sort_values(['Name', 'Season'])
	df_power['prev_HR'] = df_power.groupby('Name')['HR'].shift(1)
	df_power['prev_AB'] = df_power.groupby('Name')['AB'].shift(1)
	df_power['prev_G'] = df_power.groupby('Name')['G'].shift(1)
	df_power = df_power.dropna(subset=['prev_HR'])
	return df_power


def save_table(df: pd.DataFrame, out: str, fmt: str | None = None):
	p = Path(out)
	fmt = (fmt or '').lower()
	if fmt in ('', 'auto'):
		fmt = p.suffix.lstrip('.').lower() or 'csv'

	if fmt == 'csv':
		df.to_csv(p, index=False)
	elif fmt == 'parquet':
		df.to_parquet(p)
	elif fmt in ('xls', 'xlsx', 'excel'):
		df.to_excel(p, sheet_name='power', index=False)
	else:
		raise ValueError(f"Unsupported format: {fmt}")


def main():
	parser = argparse.ArgumentParser(description='Fetch batting stats and save processed table')
	parser.add_argument('--start', type=int, default=2016)
	parser.add_argument('--end', type=int, default=2025)
	parser.add_argument('--qual', type=int, default=1)
	parser.add_argument('--out', type=str, default='df_power.csv',
						help='Output file path (csv/parquet/xlsx)')
	parser.add_argument('--format', type=str, default='auto',
						choices=['auto', 'csv', 'parquet', 'excel', 'xls', 'xlsx'],
						help='Output format; if auto, inferred from --out')
	args = parser.parse_args()

	df_power = build_df(args.start, args.end, qual=args.qual)
	print(f"Total player-seasons: {len(df_power)}")
	print(f"Unique players: {df_power['Name'].nunique()}")

	save_table(df_power, args.out, args.format)
	print(f"Saved processed table to: {args.out}")


if __name__ == '__main__':
	main()