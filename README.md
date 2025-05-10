# 🧩 mForm ETL Pipeline (PoC) – C4GT 2025 Submission

This repository contains a Proof-of-Concept (PoC) for the **ETL Pipeline for mForm (Sync Driver)** project proposed under **C4GT 2025** with **Dhwani RIS**. 
It demonstrates two working methods to extract, transform, and load nested survey data from mForm-like structures into analytics-ready relational formats.

---

## 📌 Project Overview

**mForm** is a MERN-stack based data collection tool used by NGOs and development teams. Survey submissions in mForm are stored as deeply nested JSON structures, making them difficult to analyze directly.

This ETL pipeline solves the problem by:

- **Extracting** structured survey data
- **Transforming** nested JSON into:
  - A **master table** for non-repeating fields
  - One or more **child tables** for repeating groups
- **Loading** the results into clean CSV files (or future SQL/DBT targets)
- **Supporting incremental sync** to avoid duplicate processing

---

## 🧪 Implemented PoCs

The pipeline has been implemented using two methods:

### 1️⃣ Sample API-Based ETL  
📁 [`/mform_etl_poc(Sample API)`](./mform_etl_poc(Sample%20API))  
- Extracts data from a sample REST API that mimics mForm submissions.
- Tracks last processed ID using `last_processed_id.txt`
- Output: CSVs for master and child tables

### 2️⃣ Local Nested JSON-Based ETL  
📁 [`/mform_etl_poc`](./mform_etl_poc)  
- Loads survey data from a local sample JSON file
- Parses deeply nested structures using hierarchical traversal
- Output: Clean relational tables in CSV format

---

## 🚀 Features Implemented

| Feature                                             | Status   |
|----------------------------------------------------|----------|
| Data extraction (API / local JSON)                 | ✅ Done  |
| Flatten nested JSON into master/child tables       | ✅ Done  |
| Incremental sync using last_processed_id.txt       | ✅ Done  |
| Export to CSV                                       | ✅ Done  |
| Modular pipeline (Extractor, Transformer, Loader)  | ✅ Done  |
| File-based tracking and CLI structure              | ✅ Done  |
| Project-specific README files                      | ✅ Done  |

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Pandas** for data manipulation and CSV export
- **Requests** (API PoC only)
- **File-based sync tracking** via `last_processed_id.txt`

---

## 📊 Future Enhancements

1. Replace static input with real mForm MongoDB/REST API integration
2. Add export to SQL (PostgreSQL/MySQL) and DBT
3. Add support for config-driven mapping
4. Add CLI arguments and scheduling with cron/Airflow
5. Add schema validation and logging dashboard

