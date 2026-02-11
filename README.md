Step 1 — Project Architecture
Internet (IndiaMART)
        │
        ▼
Crawler (Scrapy / Requests / BeautifulSoup)
        │
        ▼
Raw Data (JSON)
        │
        ▼
ETL Pipeline (Clean + Transform)
        │
        ▼
Structured Data (CSV / Pandas DataFrame)
        │
        ▼
EDA + Visualization
        │
        ▼
Insights + Charts
------------------------
Step 2 — Recommended Tech Stack

Use this exact stack:

Component	Tool
Language	Python 3.10+
Scraping	requests + BeautifulSoup
Data handling	pandas
Visualization	matplotlib + seaborn
Storage	CSV + JSON
Optional advanced	Scrapy
-----------------------
requirements.txt ------->
requests
beautifulsoup4
pandas
matplotlib
seaborn






-----------------------------------------
README.md (VERY IMPORTANT FOR EVALUATION)
# Slooze Data Engineering Challenge

## Setup

pip install -r requirements.txt

## Run crawler

cd crawler
python crawler.py

## Run ETL

cd etl
python transform.py

## Run EDA

cd eda
python analysis.py
