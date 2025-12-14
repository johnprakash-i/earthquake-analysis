# 🌍 Global Seismic Trends: Data-Driven Earthquake Insights

## 📌 Project Overview

**Global Seismic Trends: Data-Driven Earthquake Insights** is an end-to-end data analytics project focused on analyzing global earthquake activity using real-time and historical seismic data.  
The project leverages  robust preprocessing, SQL-driven analytics, and interactive visualization to uncover seismic patterns, trends, and potential risk zones across the globe.

This solution is designed to support **data-driven decision-making** in disaster management, urban planning, insurance risk assessment, and geoscience research.

---

## 🌐 Domain

- **Disaster Management**
- **Geoscience**
- **Seismology**

Earthquakes pose significant risks to life and infrastructure. Understanding seismic trends and patterns enables governments, researchers, and organizations to improve preparedness, resilience, and emergency response strategies.

---

## 🛠️ Tech Stack

### Core Technologies
- **Python** – Primary language for data processing and analytics
- **Pandas** – Data cleaning, transformation, and analysis
- **NumPy** – Numerical operations
- **Regular Expressions (Regex)** – Text cleaning and parsing
- **MySQL** – Relational database for structured storage and querying
- **Streamlit** – Interactive dashboard and visualization

### Supporting Tools
- **USGS Earthquake API** – Data source
- **Jupyter Notebook** – Exploratory data analysis and preprocessing
- **SQL** – Analytical queries and trend extraction

---

## 🎯 Problem Statement

Analyze and interpret global earthquake data to:
- Identify seismic patterns and trends
- Classify earthquakes based on depth and magnitude
- Detect high-risk seismic zones
- Enable data-driven insights using structured SQL analytics

Build a scalable system using **API-based data retrieval**, **Python preprocessing**, and **SQL-driven analysis** to generate meaningful earthquake intelligence.

---

## 💼 Business Use Cases

- Assess earthquake risk for **governments and urban planners**
- Support **insurance risk modeling**
- Aid **researchers** in seismic trend analysis
- Improve **disaster preparedness and emergency response**
- Enable data-driven policies for **infrastructure resilience**

---

## 🔄 Project Workflow

1. Fetch global earthquake data from the **USGS API**
2. Clean and preprocess raw data using Python
3. Engineer new analytical features (year, month, depth category)
4. Store structured data in **MySQL**
5. Perform SQL-based analytical exploration
6. Visualize insights using **Streamlit**

---



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/johnprakash-i/earthquake-analysis.git
cd earthquake-analysis

```

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv eqvenv
eqvenv\Scripts\activate 
```     

### 3️⃣ Install Dependencies

```bash 
pip install -r requirements.txt
```

## 📥 Data Ingestion

### 4️⃣ Fetch Earthquake Data (Last 5 Years)

Navigate to the `scripts` folder and run:

```bash
python fetch_eq_data.py

```

## 🧹 Data Preprocessing

### 5️⃣ Preprocess Data (Notebook)

### Description

This step focuses on cleaning, transforming, and enriching the raw earthquake data to make it suitable for database storage and analytical processing.

Open the preprocessing notebook inside the `notebook` folder:

```bash
jupyter notebook data_preparation.ipynb

```


## 🗄️ Database Setup

### 6️⃣ Create MySQL Tables

Ensure that **MySQL** is running and properly configured before proceeding.

From the **project root directory**, execute the following command:

```bash
python migrate.py

```

### 7️⃣ Insert Data into MySQL

After table creation, load the cleaned dataset into the database by running:

```bash
python scripts/data_insert_to_table.py
```

# 📊 Analytics & Visualization
### 8️⃣ Run Streamlit Dashboard

Launch the interactive dashboard using the following command:

```bash 
streamlit run app.py

```

### 📬 Contact

For queries, collaboration opportunities, or feedback, feel free to connect.
