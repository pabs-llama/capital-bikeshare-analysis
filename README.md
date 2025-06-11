# 🚴 Capital Bikeshare Demand Analysis

This project analyzes **bike ride demand** of Capital Bikeshare (CaBi) system in the Washington DC and Metropolitan area using spatial features.  
It explores how **bike station location** and it's **proximity** to other bike stations, public transport, commercial corridors, etc. influence ride volume.

## 📌 Project Overview

- 📍 **Primary Objectives:** 
  1) Analize the relationship (if any) between geographical location of a given station and ride demand
  2) Predict ride demand for given stations in a determined period of time
  3) Guide policy decision in station placement

## 🗃️ Data Sources

- **[Capital Bikeshare Trip Data (2021–2024)](https://s3.amazonaws.com/capitalbikeshare-data/index.html)**  
  Official trip logs for all Capital Bikeshare stations across Washington, DC and surrounding metro areas.  
  > Data is freely available and can be downloaded directly from the CaBi website.

- **[Washington, DC Open Data Portal](https://opendata.dc.gov/datasets)**  
  Geospatial datasets including public transport locations, neighborhood boundaries, bike lanes, landmarks, and population metrics.

- **[Greater Greater Washington Article](https://ggwash.org/view/97701/cabi-is-a-huge-success-will-its-structure-allow-it-to-keep-growing-regionally)**  
  Commentary and urban analysis that helped frame regional disparities, especially in Prince George’s County.

---

## 📥 Dataset Access

Due to GitHub file size limitations, the full cleaned datasets used in this project (~2 GB total) are hosted externally:

- 📅 **2021–2023 Data**  
  🔗 [Download CSV (Google Drive)](https://drive.google.com/file/d/1JTO4Mu5q9UZhrPGEk9BUzcgcsIVPBfew/view?usp=drive_link)

- 📅 **2024 Data**  
  🔗 [Download CSV (Google Drive)](https://drive.google.com/file/d/1JTO4Mu5q9UZhrPGEk9BUzcgcsIVPBfew/view?usp=drive_link)

> If you prefer, you can also download the raw trip data directly from [Capital Bikeshare’s official data portal](https://s3.amazonaws.com/capitalbikeshare-data/index.html) and run the preprocessing steps from the included notebooks.

## About Cabi
Capital Bikeshare is a bike-sharing company that operates in the Washington, D.C. metropolitan area, including parts of Virginia and Maryland. It provides a network of docked bicycles that users can rent for short trips. 

## Share of CaBi rides and Stations per Region

![alt text](images/image-1.png)

## ❓ Triggering Questions

- What factors make some bike stations busier than others?
- Are high-demand stations located near specific urban features (e.g., metro stations, commercial corridors)?
- Why does Capital Bikeshare perform significantly better in Washington, DC compared to Maryland?

After initial exploration, I focused on **Prince George’s County, Maryland**, which has notably lower ridership. This regional contrast offered a compelling lens to explore how geography and infrastructure influence bikeshare demand.

## 📊 Prince George's County vs Washington, DC

|                      | **Prince George**       | **Washington, DC**     |
|----------------------|-------------------------|-------------------------|
| **Population**       | 946,971                 | 671,803                 |
| **Density**          | 757.9 / km²             | 4,355.39 / km²          |
| **CaBi Stations**    | 27                      | 395                     |

---

## 🔍 Methodology

### Data Collection
- Compiled geospatial data for bikeshare stations, metro stops, POIs, city center distance, and population density
### Feature Engineering
- Calculated distances between stations and nearby features
- Aggregated weekly ride data by station
### Visualizing
- Generated an interactive layered map with the features of interest
### Modeling
- Trained a Random Forest Regressor to predict weekly ride demand
- Evaluated using MAE and R²

---
## 🗺️ Interactive Map Preview

![alt text](images/interactive_map_preview.png)

🔗 [Click here to explore the full interactive map](https://pabs-llama.github.io/capital-bikeshare-analysis/interactive_cabi_map.html)

## 🔍 Key Insights

- CaBi Stations closer to each other, to metro and other POIs consistently show higher demand:

![alt text](images/weekly_rides_distance.png)

- In Prince George’s County, station density is low and lacks the coherence necessary for high usage. Many dockless bikes (in white) and isolated docks (red), making bikeshare less viable than driving or walking. 

![alt text](images/image-2.png)
Top: Bikeshare in western Prince George’s County (Maryland) / Bottom: Cabi in Washington, D.C

### 🔍 Model Results
- **Model**: Random Forest Regressor  
- **Target**: Weekly ride demand per station (2022–2024)  
- **Region**: Prince George’s County  
- **Features**: Distance to other stations, metro, POIs

**Performance:**

- 🧮 Mean Absolute Error (MAE): 4.49  
- 📈 Mean Weekly Rides: 16.33  
- 📊 Standard Deviation of Weekly Rides: 19.25  
- 🔍 R² Score: 0.87 — the model explains 87% of the variance

The model performs well: MAE is much smaller than the data’s natural variability.

---

## Actionable insights:

1. **Top 10% Stations**  
   Ensure high-demand stations have enough bikes/docks. Add nearby stations if existing ones are often full.

![alt text](images/predicted_demand.png)

2. **Metro-Adjacent Expansion**  
   Prioritize station placement near metro or major public transport hubs.

3. **Underperforming Stations**  
   Analyze low-use stations based on location. Consider relocation or marketing incentives to improve usage.

## 🧪 Tools & Techniques

- **Libraries**: pandas, geopandas, folium, matplotlib, scikit-learn, geopy  
- **Techniques**: distance calculations, time series aggregation, geospatial analysis, machine learning, clustering

---

## 🔍 Notebooks of Interest

- `01_EDA.ipynb`: Performs exploratory data analysis on bikeshare usage trends, station activity, and spatial distributions.
- `02_CaBi_2024`: Downloads, cleans, and preprocesses Capital Bikeshare trip data for the year 2024.
- `03_folium_mapping.ipynb`: Creates interactive layered maps using GeoPandas and Folium to visualize stations, metro stops, and points of interest.
- `04_distance_features.ipynb`: Calculates distances between bikeshare stations and nearby features (metro, landmarks, etc.) using GeoPandas and geopy.
- `05_ml_modeling.ipynb`: Uses the engineered features to train machine learning models that predict weekly ride demand.

## 🛠 Environment Setup

Follow these steps to set up your development environment:

1. **Clone the repository:**
```bash
  git clone https://github.com/yourusername/capital-bikeshare-analysis.git
  cd capital-bikeshare-analysis 
```  
2. **Create the Conda environment:**

Make sure you have Conda installed, then run:
```bash
conda env create -f environment.yml
```
3. ** Activate Environment**
```bash
conda activate capital-bikeshare-env
```
4. Launch JupyterLab:
```bash
jupyter lab
```
**Note:** This project uses the following key packages:

folium==0.19.7

geopandas==1.1.0

geopy==2.4.1

numpy==2.3.0

pandas==2.3.0

Shapely==2.1.1


## 📂 Project Structure

```bash
capital-bikeshare-analysis/
├── data/                 # Raw and processed data files
├── docs/                 # Project documentation
├── images/               # Maps and figures used in README
├── notebooks/            # Jupyter notebooks (EDA, modeling, mapping)
├── src/                  # Helper functions and scripts
├── environment.yml       # Conda environment definition
└── README.md
```
