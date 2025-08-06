import pandas as pd
import numpy as np

def analyze_csv(file_path: str) -> dict:
    df = pd.read_csv(file_path)
    basic = {
        "filename": file_path,
        "shape": df.shape,
        "dtypes": df.dtypes.astype(str).to_dict(),
        "memory_MB": round(df.memory_usage(deep=True).sum() / (1024**2), 2)
    }
    missing = {
        col: {"count": int(df[col].isnull().sum()),
              "percent": round(df[col].isnull().mean()*100, 2)}
        for col in df.columns if df[col].isnull().any()
    }
    dup = int(df.duplicated().sum())

    num = df.select_dtypes(include=[np.number])
    num_stats = num.describe().to_dict()
    outliers = {}
    for col in num:
        q1, q3 = num[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
        outliers[col] = int(df[(df[col] < lower) | (df[col] > upper)].shape[0])

    cat = df.select_dtypes(include=["object"])
    cat_stats = {}
    for col in cat:
        mode = df[col].mode()
        cat_stats[col] = {
            "unique": int(df[col].nunique()),
            "top": mode.iloc[0] if not mode.empty else None,
            "top_freq": int(df[col].value_counts().iloc[0]) if not df[col].value_counts().empty else 0
        }

    corr = num.corr().to_dict() if num.shape[1] > 1 else {}

    return {
        "basic_info": basic,
        "missing_values": missing,
        "duplicate_rows": dup,
        "numerical_stats": num_stats,
        "outlier_counts": outliers,
        "categorical_stats": cat_stats,
        "correlation_matrix": corr
    }

# if __name__ == "__main__":
#     print(analyze_csv(r"data\canada_per_capita_income.csv"))