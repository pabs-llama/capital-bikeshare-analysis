# eda_helpers.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# BASIC INSPECTION FUNCTIONS
# ----------------------------
def dataset_overview(df):
    print(f"Shape: {df.shape}")
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print(f"\nDuplicates: {df.duplicated().sum()}")

def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(' ', '_')
                  .str.replace(r'[^\w\s]', '', regex=True)
    )
    return df

# --------------------------
# MISSING VALUES
# --------------------------
def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * mis_val / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table = mis_val_table.rename(columns={0: 'Missing Values', 1: '% of Total Values'})
    return mis_val_table[mis_val_table['Missing Values'] > 0].sort_values('% of Total Values', ascending=False)

def plot_missing_values(df):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Values Heatmap")
    plt.show()

# --------------------------
# NUMERIC SUMMARY
# --------------------------
def numerical_summary(df):
    desc = df.describe().T
    desc['skew'] = df.skew(numeric_only=True)
    desc['kurtosis'] = df.kurtosis(numeric_only=True)
    return desc

def plot_numeric_distributions(df, numeric_cols=None):
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()

def remove_outliers_iqr(df, columns, factor=1.5):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[col] >= Q1 - factor * IQR) & (df[col] <= Q3 + factor * IQR)]
    return df

# --------------------------
# CATEGORICAL FEATURES
# --------------------------
def categorical_summary(df):
    cat_cols = df.select_dtypes(["object","category"])
    for col in cat_cols.columns:
        print(f"Number of unique values in {col} column: ", cat_cols[col].nunique())
    

def plot_categorical_counts(df, cat_cols=None):
    if cat_cols is None:
        cat_cols = df.select_dtypes(include='category').columns
    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=df[col], order=df[col].value_counts().index)
        plt.title(f'Count of {col}')
        plt.show()

# --------------------------
# TARGET VARIABLE
# --------------------------
def target_distribution(df, target_col):
    if df[target_col].dtype == 'object' or df[target_col].nunique() < 20:
        sns.countplot(x=target_col, data=df)
    else:
        sns.histplot(df[target_col], kde=True)
    plt.title(f'Distribution of {target_col}')
    plt.show()

# --------------------------
# CORRELATION / COLLINEARITY
# --------------------------
def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()

def top_correlations(df, target, method='pearson', n=5):
    corr = df.corr(method=method)[target].drop(target)
    return corr.abs().sort_values(ascending=False).head(n)

def multicollinearity_pairs(df, threshold=0.8):
    corr_matrix = df.corr(numeric_only=True).abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    return [(col, idx, upper.loc[idx, col]) for col in upper.columns for idx in upper.index if upper.loc[idx, col] > threshold]

# --------------------------
# DATE/TIME FEATURES
# --------------------------
def convert_to_datetime(df, cols):
    for col in cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

def extract_datetime_parts(df, datetime_cols):
    for col in datetime_cols:
        df[f'{col}_year'] = df[col].dt.year
        df[f'{col}_month'] = df[col].dt.month
        df[f'{col}_day'] = df[col].dt.day
        df[f'{col}_weekday'] = df[col].dt.weekday
        df[f'{col}_hour'] = df[col].dt.hour
    return df

# --------------------------
# OTHER UTILITIES
# --------------------------
def reduce_memory_usage(df):
    for col in df.select_dtypes(include=['int', 'float']).columns:
        col_min = df[col].min()
        col_max = df[col].max()
        if pd.api.types.is_integer_dtype(df[col]):
            if col_min >= 0:
                if col_max < 255:
                    df[col] = df[col].astype(np.uint8)
                elif col_max < 65535:
                    df[col] = df[col].astype(np.uint16)
                else:
                    df[col] = df[col].astype(np.uint32)
            else:
                df[col] = df[col].astype(np.int32)
        else:
            df[col] = df[col].astype(np.float32)
    return df

def find_duplicates(df, subset=None):
    return df[df.duplicated(subset=subset, keep=False)]

def group_summary(df, groupby_col, target_col):
    return df.groupby(groupby_col)[target_col].agg(['count', 'mean', 'median', 'std']).sort_values('count', ascending=False)

def feature_cardinality(df, threshold=50):
    return {col: df[col].nunique() for col in df.columns if df[col].nunique() > threshold}

def find_rare_labels(df, col, threshold=0.01):
    value_counts = df[col].value_counts(normalize=True)
    return value_counts[value_counts < threshold].index.tolist()
