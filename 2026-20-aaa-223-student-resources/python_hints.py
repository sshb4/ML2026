#!/usr/bin/env python3
"""
CS 4320 — Assignment 3 (Part A) HINTS
Ames Housing (curated) — starter + hints script (NO scikit-learn)

This file is designed to help you get unstuck without giving away the full solution.
You are still responsible for implementing the required steps and writing up what you did.

Rules reminder:
- You MAY use numpy/pandas for array/data operations.
- You may NOT use scikit-learn to do splitting, imputation, scaling, or encoding.

Recommended workflow (leakage-safe):
1) Load data
2) Split into train/val/test with the required seed
3) Separate target y from features X
4) Fit preprocessing on TRAIN ONLY:
   - numeric median
   - categorical mode
   - scaling mean/std
   - one-hot categories
5) Apply those artifacts to val/test
"""

import numpy as np
import pandas as pd

CSV_PATH = "../df_power.csv"
SEED = 4320  # required seed (so everyone gets the same split)

TARGET_COL = "HR"

# You should decide which columns are safe/appropriate to use as model inputs.
# (Hint: identifiers are usually not appropriate.)
POSSIBLE_EXCLUDES = ["IDfg", "Name", "Season", TARGET_COL]


def split_indices(n: int, seed: int, train_frac: float = 0.70, val_frac: float = 0.15):
    """Deterministic split using a seeded permutation (same idea as lecture)."""
    rng = np.random.default_rng(seed)
    perm = rng.permutation(n)

    n_train = int(round(train_frac * n))
    n_val = int(round(val_frac * n))

    train_idx = perm[:n_train]
    val_idx = perm[n_train:n_train + n_val]
    test_idx = perm[n_train + n_val:]
    return train_idx, val_idx, test_idx


def main():
    df = pd.read_csv(CSV_PATH)

    # 1) Split
    train_idx, val_idx, test_idx = split_indices(len(df), SEED)

    train_df = df.iloc[train_idx].copy()
    val_df   = df.iloc[val_idx].copy()
    test_df  = df.iloc[test_idx].copy()

    # 2) Separate target
    y_train = train_df[TARGET_COL].to_numpy(dtype=float)
    y_val   = val_df[TARGET_COL].to_numpy(dtype=float)
    y_test  = test_df[TARGET_COL].to_numpy(dtype=float)

    # 3) Choose feature columns (drop target + other columns you believe should be excluded)
    X_train = train_df.drop(columns=[c for c in POSSIBLE_EXCLUDES if c in train_df.columns])
    X_val   = val_df.drop(columns=[c for c in POSSIBLE_EXCLUDES if c in val_df.columns])
    X_test  = test_df.drop(columns=[c for c in POSSIBLE_EXCLUDES if c in test_df.columns])

    # 4) Identify numeric vs categorical
    numeric_cols = [c for c in X_train.columns if pd.api.types.is_numeric_dtype(X_train[c])]
    cat_cols = [c for c in X_train.columns if c not in numeric_cols]

    # 5) FIT imputation on TRAIN ONLY
    # TODO: compute numeric medians from X_train
    numeric_medians = X_train[numeric_cols].median()
    # TODO: compute categorical modes from X_train
    if cat_cols:
        categorical_modes = X_train[cat_cols].mode().iloc[0]
    else:
        categorical_modes = pd.Series(dtype=object)
    
    # Store for reporting
    numeric_medians_report = numeric_medians.copy()
    categorical_modes_report = categorical_modes.copy()
    
    # Then apply to X_train / X_val / X_test using fillna()
    X_train[numeric_cols] = X_train[numeric_cols].fillna(numeric_medians)
    X_val[numeric_cols] = X_val[numeric_cols].fillna(numeric_medians)
    X_test[numeric_cols] = X_test[numeric_cols].fillna(numeric_medians)

    if cat_cols:
        X_train[cat_cols] = X_train[cat_cols].fillna(categorical_modes)
        X_val[cat_cols] = X_val[cat_cols].fillna(categorical_modes)
        X_test[cat_cols] = X_test[cat_cols].fillna(categorical_modes)

    # 6) FIT scaling on TRAIN ONLY (numeric only)
    # TODO: compute mean/std from *imputed* X_train
    numeric_means = X_train[numeric_cols].mean()
    numeric_stds = X_train[numeric_cols].std()
    
    # Store for reporting
    numeric_means_report = numeric_means.copy()
    numeric_stds_report = numeric_stds.copy()
    
    # TODO: apply (x - mean) / std to X_train / X_val / X_test
    X_train[numeric_cols] = (X_train[numeric_cols] - numeric_means) / numeric_stds
    X_val[numeric_cols] = (X_val[numeric_cols] - numeric_means) / numeric_stds
    X_test[numeric_cols] = (X_test[numeric_cols] - numeric_means) / numeric_stds

    # 7) FIT one-hot categories on TRAIN ONLY
    # TODO: build a list of categories per categorical column from X_train
    categories = {c: sorted(X_train[c].unique()) for c in cat_cols}  # sorted for deterministic order
    
    # Store for reporting
    categories_report = categories.copy()
    
    # TODO: create one-hot columns in a deterministic order
    for c in cat_cols:
        for cat in categories[c]:
            X_train[f"{c}_{cat}"] = (X_train[c] == cat).astype(int)
            X_val[f"{c}_{cat}"] = (X_val[c] == cat).astype(int)
            X_test[f"{c}_{cat}"] = (X_test[c] == cat).astype(int)
        #Drop original categorical columns
        X_train = X_train.drop(columns=[c])
        X_val = X_val.drop(columns=[c])
        X_test = X_test.drop(columns=[c])
    # IMPORTANT: unseen categories in val/test automatically map to all-zeros
    # (because they don't match any category in the training set)

    # Final: produce numpy arrays
    # TODO: concatenate scaled numeric + one-hot categorical into final matrices
    X_train_np = X_train.to_numpy()
    X_val_np = X_val.to_numpy()
    X_test_np = X_test.to_numpy()

    print("=" * 70)
    print("SPLIT SIZES")
    print("=" * 70)
    print(f"Training set: {len(train_df)} rows ({len(train_df)/len(df)*100:.1f}%)")
    print(f"Validation set: {len(val_df)} rows ({len(val_df)/len(df)*100:.1f}%)")
    print(f"Test set: {len(test_df)} rows ({len(test_df)/len(df)*100:.1f}%)")
    
    print("\n" + "=" * 70)
    print("FEATURE TYPES")
    print("=" * 70)
    print(f"Numeric features ({len(numeric_cols)}): {numeric_cols}")
    print(f"Categorical features ({len(cat_cols)}): {cat_cols}")
    
    print("\n" + "=" * 70)
    print("PREPROCESSING ARTIFACTS (fitted on train only)")
    print("=" * 70)
    print("\nImputation values:")
    print(f"  Numeric medians: {dict(numeric_medians_report)}")
    if cat_cols:
        print(f"  Categorical modes: {dict(categorical_modes_report)}")
    else:
        print("  No categorical columns to impute.")
    
    print("\nScaling parameters:")
    print(f"  Numeric means: {dict(numeric_means_report.round(2))}")
    print(f"  Numeric stds: {dict(numeric_stds_report.round(2))}")
    
    print("\nOne-hot encoding:")
    for col in cat_cols:
        print(f"  {col}: {len(categories_report[col])} categories → {categories_report[col][:5]}{'...' if len(categories_report[col]) > 5 else ''}")
    
    print("\n" + "=" * 70)
    print("FINAL SHAPES & SANITY CHECKS")
    print("=" * 70)
    print(f"X_train: {X_train_np.shape}, y_train: {y_train.shape}")
    print(f"X_val:   {X_val_np.shape}, y_val:   {y_val.shape}")
    print(f"X_test:  {X_test_np.shape}, y_test:  {y_test.shape}")
    
    print("\nFeature statistics after preprocessing (train set):")
    print(f"  Mean of scaled features: {X_train_np.mean(axis=0)[:5].round(4)} (should be ~0)")
    print(f"  Std of scaled features: {X_train_np.std(axis=0)[:5].round(4)} (should be ~1)")
    print(f"  Min value in train: {X_train_np.min():.2f}")
    print(f"  Max value in train: {X_train_np.max():.2f}")
    
    print("\nTarget HR statistics:")
    print(f"  Train - mean: {y_train.mean():.1f}, std: {y_train.std():.1f}, range: {y_train.min():.0f} - {y_train.max():.0f}")
    print(f"  Val   - mean: {y_val.mean():.1f}, std: {y_val.std():.1f}, range: {y_val.min():.0f} - {y_val.max():.0f}")
    print(f"  Test  - mean: {y_test.mean():.1f}, std: {y_test.std():.1f}, range: {y_test.min():.0f} - {y_test.max():.0f}")
    
    print("\n" + "=" * 70)
    print("LEAKAGE PREVENTION VERIFICATION")
    print("=" * 70)
    print("✓ IDfg, Name, Season excluded from features")
    print("✓ All preprocessing fitted on train only")
    print("✓ Test set never used to calculate statistics")
    print("=" * 70)


if __name__ == "__main__":
    main()
