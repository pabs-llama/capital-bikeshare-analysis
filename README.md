# 🚴 Capital Bikeshare Demand Analysis

This project analyzes **bike ride demand** in the Washington DC Capital Bikeshare system using spatial features.  
It explores how **station location**, **metro proximity**, and **urban zones (DC vs Maryland)** influence ride volume.

---

## 📌 Project Overview

- 📍 **Goal:** Predict ride demand at Capital Bikeshare stations using geospatial data
- 🗃️ **Data Sources:**
  - Capital Bikeshare trip data (https://s3.amazonaws.com/capitalbikeshare-data/index.html)
  - Geographic features Washington DC metro station locations (GeoJSON)

---

## 🔍 Key Insights

- Stations closer to metro hubs have consistently higher demand
- Urban density impact ridership

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
