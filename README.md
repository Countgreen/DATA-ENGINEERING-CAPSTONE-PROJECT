# 📊 Scalable Data Engineering Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Project](https://img.shields.io/badge/Project-Data%20Engineering-blueviolet)

---

## 🚀 Project Overview

The **Scalable Data Engineering Pipeline** is an end-to-end data processing system that simulates real-world data engineering workflows including ingestion, transformation, storage, validation, and visualization.

This project demonstrates how modern data pipelines work using real-world financial data and integrates key concepts like streaming, ETL/ELT, distributed systems, and analytics dashboards.

---

## 🏗️ System Architecture

```mermaid
flowchart LR
A[Real Dataset CSV] --> B[Streaming Simulation]
B --> C[Data Ingestion (Pandas)]
C --> D[Data Processing]

D --> D1[Cleaning]
D --> D2[Rolling Average]
D --> D3[Normalization]
D --> D4[Large Data Simulation]

D --> E[Storage Layer (CSV/Data Lake)]

E --> F[Data Quality Checks]
F --> F1[Null Checks]
F --> F2[Anomaly Detection]

F --> G[Distributed Systems Simulation]

G --> G1[Hadoop (Data Splitting)]
G --> G2[Spark (Partitioning)]
G --> G3[Kafka (Streaming Simulation)]
G --> G4[Airflow (Scheduling)]

G --> H[Analytics Layer]

H --> H1[KPI Calculation]
H --> H2[Trend Detection]
H --> H3[Prediction]

H --> I[Streamlit Dashboard]
```

## ⚙️ Tech Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy

### Visualization
- Streamlit

### Database
- SQLite

### Concepts & Tools
- ETL / ELT Pipelines
- Data Warehousing
- Streaming Systems
- Distributed Systems (Simulated)
- Data Quality & Validation

---

## 📂 Project Structure

```
project/
│
├── data/
├── ingestion/
├── processing/
├── streaming/
├── sql/
├── etl_elt/
├── hadoop_sim/
├── spark_sim/
├── airflow_sim/
├── cloud/
├── lakehouse/
├── quality/
├── dashboard/
│
├── main.py
└── requirements.txt
```

---

## 🧠 Data Engineering Pipeline

### 1️⃣ Data Source
- Real-world financial dataset (CSV)

### 2️⃣ Streaming Simulation
- Sequential data streaming to mimic real-time systems

### 3️⃣ Data Ingestion
- CSV loading and merging using Pandas

### 4️⃣ Data Processing
- Data cleaning
- Rolling average calculation
- Normalization
- Large dataset simulation

### 5️⃣ Data Storage
- Stored in CSV (Data Lake simulation)

### 6️⃣ Data Quality & Validation
- Null checks
- Anomaly detection

### 7️⃣ Distributed Systems (Simulated)
- Hadoop → Data splitting
- Spark → Partitioning
- Kafka → Streaming simulation
- Airflow → Scheduling

### 8️⃣ Analytics Layer
- KPI calculation (avg, max, min)
- Trend detection
- Prediction

### 9️⃣ Visualization
- Interactive dashboard using Streamlit

---

## 📊 Dashboard Preview

![Dashboard](./assets/dashboard.png)

---

## 🔍 Output

- Real data streaming simulation  
- Processed dataset  
- Analytical insights  
- Dashboard visualization  

---

## ▶️ Installation and Setup

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python streaming/stream.py
python main.py
streamlit run dashboard/app.py
```

---

## 🧪 Use Cases

- Data Engineering projects  
- Real-time pipeline simulation  
- Analytics dashboards  
- Academic submissions  

---

## 🔮 Future Improvements

- Real Kafka & Hadoop integration  
- Cloud deployment (AWS / GCP)  
- Real-time APIs  
- ML-based predictions  

---

## 👨‍💻 Author

**Harsh Verma**  
CSE Student | Data Engineering Enthusiast  

---

## 📜 License

This project is for academic purposes.
