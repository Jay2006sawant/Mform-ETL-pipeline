🧩 mForm ETL Pipeline (Sample Nested JSON PoC)

This is a Proof-of-Concept (PoC) ETL pipeline for the mForm Sync Driver project under Dhwani RIS. It demonstrates how to extract nested survey data from a **local sample JSON file**, transform it into clean relational tables (master and child), and export the results to CSV.

---

📌 Project Overview

Many NGOs using mForm, a MERN-stack survey tool, face challenges in converting deeply nested JSON form submissions into analytics-friendly formats. This ETL pipeline solves that problem by:

- Loading data from a **sample nested JSON file** (`sample_data.json`) that simulates mForm’s survey submission format.
- Transforming the JSON:
  - Non-repeating fields → `master_table.csv`
  - Repeating groups (e.g., household members, group questions) → `child_table_<group>.csv`
- Exporting the transformed data into flat CSVs (ready for SQL or visualization).
- Supporting **incremental sync** using a `last_processed_id.txt` tracker.

---

🚀 Features Implemented

| Feature                                           | Status    |
|--------------------------------------------------|-----------|
| Load from sample nested JSON file                | ✅ Done   |
| Flatten nested JSON to master/child tables       | ✅ Done   |
| Incremental sync using last processed ID         | ✅ Done   |
| Export to CSV                                     | ✅ Done   |
| Modular code (Extractor, Transformer, Loader)    | ✅ Done   |
| File-based state tracking                        | ✅ Done   |
| CLI-ready structure via `main.py`                | ✅ Done   |

---

🔧 Tech Stack

- **Python 3.10+**
- **Pandas** for data transformation and CSV output
- **Local JSON file** (`data/sample_input.json`) as input
---