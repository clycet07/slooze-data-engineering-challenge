slooze-data-engineering/
│
├── crawler/
│   ├── crawler.py
│   └── utils.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── etl/
│   └── transform.py
│
├── eda/
│   └── analysis.py
│
├── requirements.txt
└── README.md

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
