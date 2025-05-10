# mForm ETL Pipeline – Sample Nested JSON PoC

This project is a **Proof of Concept (PoC)** for an ETL (Extract, Transform, Load) pipeline designed for [mForm](https://www.dhwaniris.org/mform), a digital data collection platform used by NGOs. This PoC demonstrates how to process **complex nested JSON survey submissions** and convert them into flat, analysis-ready CSV tables.

📌 This PoC uses **sample nested JSON data stored locally** (`sample_data.json`) to simulate real-world mForm survey submissions.

---

## 📚 Overview

The ETL pipeline performs the following:

- **Extraction**: Loads sample nested JSON data from a local file.
- **Transformation**: Flattens the JSON into:
  - A **master table** for non-repeating fields.
  - **Child tables** for repeating groups (e.g. group of questions or household members).
- **Loading**: Saves the transformed data into structured CSV files.