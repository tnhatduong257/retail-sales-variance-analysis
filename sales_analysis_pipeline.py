import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def generate_business_data(n_rows: int = 100000, seed: int = 42) -> pd.DataFrame:
    """
    Generates simulated daily sales and customer traffic data across different regions.

    Args:
        n_rows (int): The number of records to generate. Defaults to 100,000.
        seed (int): Random seed for reproducibility.

    Returns:
        pd.DataFrame: The raw, uncleaned dataset.
    """
    rng = np.random.default_rng(seed=seed)
    
    # 1. Generate store identifiers and assign regions
    store_ids = rng.integers(1, 51, size=n_rows)
    regions = rng.choice(["North", "South", "West", "East"], size=n_rows)
    
    # 2. Map business characteristics (Mean and Standard Deviation) to each region
    region_series = pd.Series(regions)
    means = region_series.map({'North': 7500, 'South': 3200, 'East': 5000, 'West': 4500})
    stds = region_series.map({'North': 500,  'South': 400,  'East': 2800, 'West': 1200})
    
    # 3. Generate statistical data using vectorization
    daily_sales = rng.normal(loc=means, scale=stds) 
    customer_count = rng.poisson(lam=300, size=n_rows)
    
    # 4. Construct the DataFrame
    df = pd.DataFrame({
        "Store_ID": store_ids, 
        "Region": regions, 
        "Daily_Sales": daily_sales,
        "Customer_Count": customer_count
    })
    
    # 5. Inject random missing values (NaN) to simulate system errors
    missing_indices = rng.choice(n_rows, size=1000, replace=False)
    df.loc[missing_indices, "Daily_Sales"] = np.nan
    
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the dataset by handling missing values and filtering outliers.

    Args:
        df (pd.DataFrame): The raw input DataFrame.

    Returns:
        pd.DataFrame: The fully cleaned dataset.
    """
    df_clean = df.copy()
    
    # Impute missing values using the regional mean (Groupby Imputation)
    df_clean["Daily_Sales"] = df_clean.groupby("Region")["Daily_Sales"].transform(
        lambda x: x.fillna(x.mean())
    )
    
    # Remove records with negative sales (Outliers from Normal Distribution)
    df_clean = df_clean[df_clean["Daily_Sales"] >= 0]
    
    return df_clean

def analyze_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregates performance metrics and evaluates financial risk (variance) by region.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        pd.DataFrame: A summary report containing core business metrics.
    """
    summary = df.groupby("Region").agg(
        Total_Sales=("Daily_Sales", "sum"),
        Average_Sales=("Daily_Sales", "mean"),
        Sales_Variance=("Daily_Sales", "var"),
        Sales_StdDev=("Daily_Sales", "std"),
        Avg_Customers=("Customer_Count", "mean")
    ).reset_index()
    
    return summary

def visualize_insights(df: pd.DataFrame, summary: pd.DataFrame):
    """
    Generates and exports data visualizations for business insights.

    Args:
        df (pd.DataFrame): The detailed, cleaned dataset.
        summary (pd.DataFrame): The aggregated performance report.
    """
    # ==========================================
    # 1. Histogram (Distribution Analysis)
    # ==========================================
    plt.figure(figsize=(10, 6))
    plt.hist(df["Daily_Sales"], bins=50, color="skyblue", edgecolor="black", alpha=0.7)
    plt.title('Daily Sales Distribution (Normal Distribution)', fontsize=14, fontweight='bold')
    plt.xlabel('Sales (USD)', fontsize=12)
    plt.ylabel('Frequency (Days)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig('sales_histogram.png', dpi=300, bbox_inches='tight')
    plt.show()

    # ==========================================
    # 2. Boxplot (Variance & Risk Analysis)
    # ==========================================
    plt.figure(figsize=(10, 6))
    unique_regions = df['Region'].unique()
    sales_by_region = [df[df['Region'] == region]['Daily_Sales'] for region in unique_regions]
    
    box = plt.boxplot(sales_by_region, tick_labels=unique_regions, patch_artist=True)
    
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        
    plt.title('Sales Variance by Region (Risk Analysis)', fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Daily Sales (USD)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.savefig('regional_boxplot.png', dpi=300, bbox_inches='tight')
    plt.show()

    # ==========================================
    # 3. Bar Chart (Performance Overview)
    # ==========================================
    plt.figure(figsize=(10, 6))
    plt.bar(summary['Region'], summary['Average_Sales'], 
            color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], edgecolor='black')
    
    plt.title('Average Daily Sales by Region', fontsize=14, fontweight='bold')
    plt.xlabel('Region', fontsize=12)
    plt.ylabel('Average Sales (USD)', fontsize=12)
    
    # Add data labels on top of the bars
    for i, value in enumerate(summary['Average_Sales']):
        plt.text(i, value + 50, f"${value:,.0f}", ha='center', fontweight='bold')
        
    plt.savefig('regional_barchart.png', dpi=300, bbox_inches='tight')
    plt.show()

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Generate data
    raw_data = generate_business_data()
    
    # 2. Clean data
    clean_data_df = clean_data(raw_data)
    
    # 3. Analyze data
    regional_summary = analyze_performance(clean_data_df)
    
    # Format and print the console report
    print_summary = regional_summary.copy()
    print_summary['Total_Sales'] = print_summary['Total_Sales'].apply(lambda x: f"${x:,.2f}")
    print_summary['Average_Sales'] = print_summary['Average_Sales'].apply(lambda x: f"${x:,.2f}")
    
    print("\n=== REGIONAL PERFORMANCE SUMMARY ===")
    print(print_summary.to_string(index=False))
    print("====================================\n")
    
    # 4. Visualize data
    visualize_insights(clean_data_df, regional_summary)