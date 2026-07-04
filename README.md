# ✈️ Airline Flight Operations Dashboard

🚀 A real-time flight schedule analytics project built to demonstrate an end-to-end Business Analyst workflow — from live API data extraction to cleaning, analysis, documentation, and interactive dashboard creation.

---

## 📌 Project Overview

This project simulates a real-world airline operations analytics system using live flight data.

It covers the full workflow:

🌐 Data extraction → 🧹 Data cleaning → 📊 Analysis → 📈 Visualization → 📝 Business documentation

---

## ⚙️ What this project does

- 🌍 Extracts real-time flight data using the **AviationStack API**
- 🐍 Processes and cleans data using **Python (pandas)**
- 📊 Analyzes key metrics such as:
  - Top airlines ✈️  
  - Busiest departure airports 🛫  
  - Flight status distribution 📡  
- 📈 Visualizes insights using:
  - Power BI Dashboard 📊  
  - Custom HTML/CSS Dashboard 🌐  
- 📝 Documents complete Business Requirements (BRD) including:
  - Objectives 🎯  
  - Scope 📌  
  - Methodology ⚙️  
  - Findings 📊  
  - Data limitations ⚠️  

---

## 💡 Why this project is important

Real-world data is often incomplete or imperfect.

⚠️ The free AviationStack API used in this project returned only limited “scheduled” flight data with minimal delay information.

Because of that:

- ❌ On-time performance analysis was not possible  
- ✅ Instead of guessing, the limitation was clearly documented in the BRD  

👉 This reflects real Business Analyst practice: **transparency over assumptions**

---

## 📊 Key Insights

| Metric | Value |
|------|------|
| ✈️ Total flights captured | 100 |
| 🏢 Distinct airlines | 42 |
| 🛫 Distinct departure airports | 18 |
| 🔥 Busiest airport | Tianjin Binhai International (32%) |

---

## 📁 Project Structure
📦 Airline-Flight-Operations-Dashboard
├── 🐍 flight_data.py
│   └── API data extraction script (AviationStack)
│
├── 🧹 analyze.py
│   └── Data cleaning & analysis (pandas)
│
├── 📊 flight_data.csv
│   └── Raw dataset captured from API
│
├── 🌐 flight_operations_dashboard.html
│   └── Custom interactive dashboard (HTML/CSS)
│
├── 📄 BRD_Airline_Flight_Dashboard.docx
│   └── Full Business Requirements Document
│
└── 🔐 .env (not included in repo)
    └── API keys and sensitive credentials
