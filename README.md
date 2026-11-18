# Retail Sales Variance Analysis

A comprehensive Python data pipeline and statistical analysis tool designed to ingest, process, and analyze **100,000 simulated retail transaction records**. This project evaluates regional sales performance, uncovers variance patterns, and generates automated visual insights using Python data science libraries.

## 🚀 Key Features
* **Data Processing Pipeline:** Cleans, aggregates, and transforms large-scale transactional datasets using `Pandas` and `NumPy`.
* **Variance & Statistical Analysis:** Evaluates sales variance across multiple retail regions, product categories, and fiscal periods.
* **Automated Data Visualization:** Generates and exports publication-ready analytical charts using `Matplotlib`, including distribution histograms, regional barcharts, and comparative boxplots.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Matplotlib
* **Version Control:** Git / GitHub

---

## 📊 Visualizations & Results

### 1. Regional Sales Distribution
The pipeline automatically generates comparative charts highlighting regional performance and variance:
* **Regional Barchart:** Evaluates total sales output by geographic territory (`regional_barchart.png`).
* **Sales Histogram:** Analyzes transaction value frequency and distribution skewness (`sales_histogram.png`).
* **Regional Boxplot:** Identifies data dispersion and outliers across different operating regions (`regional_boxplot.png`).

---

## ⚙️ Getting Started & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/tnhatduong257/retail-sales-variance-analysis.git](https://github.com/tnhatduong257/retail-sales-variance-analysis.git)
   cd retail-sales-variance-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install numpy pandas matplotlib
   ```

3. **Run the analysis pipeline:**
   ```bash
   python sales_analysis_pipeline.py
   ```
