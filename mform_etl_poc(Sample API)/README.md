# 🧩 mForm ETL Pipeline (Sample API PoC)

This is a Proof-of-Concept (PoC) ETL pipeline for the **mForm Sync Driver** project under [Dhwani RIS](https://www.dhwaniris.in/). It demonstrates how to extract nested survey data from a **sample REST API**, transform it into clean relational tables (master and child), and export the results to CSV.

---

## 📌 Project Overview

Many NGOs using **mForm**, a MERN-stack survey tool, face challenges in converting deeply nested JSON form submissions into analytics-friendly formats. This ETL pipeline solves that problem by:

- **Extracting** data from a Sample API that mimics mForm’s nested JSON structure.
- **Transforming** the JSON:
  - Non-repeating fields → `master_table.csv`
  - Repeating groups → `child_table.csv`
- **Loading** the transformed data into flat CSVs (or later, to SQL databases).
- Supporting **incremental sync** using a `last_processed_id.txt` tracker.

---

## 🚀 Features Implemented

| Feature | Status |
|--------|--------|
| Extract from Sample API | ✅ Done |
| Flatten nested JSON to master/child tables | ✅ Done |
| Incremental sync using last ID | ✅ Done |
| Export to CSV | ✅ Done |
| Modular structure (Extractor, Transformer, Loader) | ✅ Done |
| Basic README and file usage guide | ✅ Done |

---

## 🔧 Tech Stack

- **Python 3.10+**
- REST API (Sample JSON endpoint)
- CSV output via `pandas`
- File-based state tracking (for incremental sync)

---

