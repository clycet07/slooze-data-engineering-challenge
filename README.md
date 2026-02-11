# Slooze Data Engineering Take-Home Challenge

## Overview

This project implements an end-to-end data engineering pipeline to collect, process, and analyze product and supplier data from a B2B marketplace (IndiaMART). The system includes a web crawler, ETL pipeline, structured data storage, and exploratory data analysis (EDA) to generate insights about supplier distribution, pricing patterns, and product trends.

This project demonstrates core data engineering competencies including web scraping, data transformation, pipeline design, and data analysis.

---

## Architecture

The pipeline follows a standard data engineering workflow:

```
Data Source (IndiaMART)
        │
        ▼
Web Crawler (requests + BeautifulSoup)
        │
        ▼
Raw Data Storage (JSON)
        │
        ▼
ETL Pipeline (Pandas)
        │
        ▼
Processed Data (CSV)
        │
        ▼
EDA & Visualization (Matplotlib, Seaborn)
        │
        ▼
Insights & Analysis
```

---

## Project Structure

```
slooze-data-engineering/
│
├── crawler/
│   ├── crawler.py
│
├── etl/
│   ├── transform.py
│
├── eda/
│   ├── analysis.py
│
├── data/
│   ├── raw/
│   │   └── products.json
│   │
│   ├── processed/
│       └── products.csv
│
├── requirements.txt
└── README.md
```

---

## Features

### Part A – Data Collection

The crawler extracts the following fields:

* Product Name
* Price
* Supplier Name
* Supplier Location
* Timestamp (optional)
* Product Category

Key design considerations:

* Uses HTTP headers to mimic real browser requests
* Includes randomized delays to avoid rate limiting
* Modular and reusable crawler design
* Outputs structured JSON data

---

### Part B – ETL Pipeline

The ETL process performs:

* Data loading from raw JSON
* Data cleaning
* Price normalization
* Duplicate removal
* Missing value handling
* Structured storage in CSV format

---

### Part C – Exploratory Data Analysis (EDA)

The analysis identifies:

* Supplier distribution by location
* Price distribution
* Most common supplier regions
* Dataset summary statistics
* Data quality issues

Visualizations include:

* Bar charts for supplier locations
* Price distribution histograms
* Summary statistics

---

## Installation

### Step 1 – Clone the repository

```
git clone https://github.com/yourusername/slooze-data-engineering-challenge.git
cd slooze-data-engineering-challenge
```

---

### Step 2 – Install dependencies

```
pip install -r requirements.txt
```

---

## How to Run

### Step 1 – Run crawler

```
cd crawler
python crawler.py
```

This generates:

```
data/raw/products.json
```

---

### Step 2 – Run ETL pipeline

```
cd ../etl
python transform.py
```

This generates:

```
data/processed/products.csv
```

---

### Step 3 – Run EDA analysis

```
cd ../eda
python analysis.py
```

This generates:

* Console statistics
* Charts and visual insights

---

## Output Files

Raw data:

```
data/raw/products.json
```

Processed data:

```
data/processed/products.csv
```

---

## Example Data Fields

```
product_name
price
supplier
location
```

---

## Insights Generated

Examples of insights derived from the dataset:

* Major supplier hubs (e.g., Ahmedabad, Mumbai, Delhi)
* Price ranges and distribution patterns
* Supplier concentration by region
* Missing or inconsistent data patterns

---

## Technologies Used

* Python 3
* requests
* BeautifulSoup
* pandas
* matplotlib
* seaborn

---

## Design Decisions

* Modular structure for maintainability
* Separation of crawler, ETL, and analysis layers
* Structured storage for downstream analytics
* Lightweight and scalable approach

---

## Scalability Improvements (Future Work)

Possible enhancements include:

* Using Scrapy framework for large-scale crawling
* Storing data in PostgreSQL or MongoDB
* Workflow orchestration using Airflow
* Deploying pipeline on AWS
* Adding incremental crawling

---

## Compliance and Ethics

The crawler respects:

* Reasonable request delays
* Publicly available data only
* No authentication bypass


---

## Conclusion

This project demonstrates a complete data engineering workflow including:

* Data collection
* Data transformation
* Structured storage
* Data analysis
* Insight generation

The implementation emphasizes clean architecture, modularity, and scalability.
