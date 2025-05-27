# 🚴 Capital Bikeshare Demand Analysis

![Capital Bikeshare Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Capital_Bikeshare_logo.svg/1200px-Capital_Bikeshare_logo.svg.png)

---

## 📖 Project Description

This project analyzes **bike ride demand** in the Washington DC Capital Bikeshare system using spatial and temporal features.  
It explores how **station location**, **metro proximity**, and **urban zones (DC vs Maryland)** influence ride volume.

---

## 📌 Project Overview

- 📍 **Goal:** Predict ride demand at Capital Bikeshare stations using geospatial and temporal data
- 📅 **Period:** [Insert date range]
- 🗃️ **Data Sources:**
  - Capital Bikeshare trip data
  - Washington DC metro station locations (GeoJSON)

---

## 🔍 Key Insights

- Stations closer to metro hubs have consistently higher demand
- Temporal trends show weekday morning/evening peaks
- Urban density and neighborhood context impact ridership

---

## 🧪 Techniques Used

- Pandas, GeoPandas, Matplotlib, Folium
- Distance calculations with geospatial data
- Time series aggregation
- Data visualization & clustering

---

## 📂 Project Structure

```bash
capital-bikeshare-analysis/
├── notebooks/               # Jupyter notebooks for EDA and modeling
├── src/                     # Utility functions (e.g., geo_distance.py)
├── data/                    # Cleaned or sample data files
├── images/                  # Output maps/graphs for README
├── requirements.txt
└── README.md
