
import pandas as pd
import geopandas as gpd
import folium
import json
from shapely.geometry import shape
from geopy.distance import geodesic

def load_bikeshare_data(path):
    data_types = {
        "rideable_type": "category", 
        "start_station_name": "category", 
        "end_station_name": "category", 
        "member_casual": "category",
        "time_of_day": "category",
        "trip_type": "category"
    }
    return pd.read_csv(path, dtype=data_types, parse_dates=["started_at", "ended_at"], low_memory=False)


def create_centered_map(df, lat_col="start_lat", lng_col="start_lng", zoom_start=12, min_zoom=2, max_zoom=26):
    """
    Creates a folium map centered on the average coordinates in a DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame containing latitude and longitude columns
        lat_col (str): Name of the latitude column
        lng_col (str): Name of the longitude column
        zoom_start (int): Initial zoom level
        min_zoom (int): Minimum zoom level
        max_zoom (int): Maximum zoom level

    Returns:
        folium.Map: Centered map
    """
    avg_lat = df[lat_col].mean()
    avg_lng = df[lng_col].mean()
    return folium.Map(
        location=[avg_lat, avg_lng],
        zoom_start=zoom_start,
        min_zoom=min_zoom,
        max_zoom=max_zoom
    )

def get_unique_station_coordinates(df):
    avg_lat = df.groupby("start_station_name", as_index=False, observed=False)["start_lat"].mean()
    avg_lng = df.groupby("start_station_name", as_index=False, observed=False)["start_lng"].mean()
    return avg_lat.merge(avg_lng)

def get_coordinates(row):
    return (row['start_lat'], row['start_lng']), (row['end_lat'], row['end_lng'])

def get_distance_km(row):
    start, end = get_coordinates(row)
    return geodesic(start, end).km


def load_geojson_as_gdf(filepath, crs="EPSG:4326"):
    """
    Loads a GeoJSON file and returns a GeoDataFrame.
    
    Parameters:
        filepath (str): Path to the GeoJSON file.
        crs (str): Coordinate Reference System, default is 'EPSG:4326'.

    Returns:
        GeoDataFrame: Geospatial dataframe with properties and geometry.
    """
    with open(filepath, 'r') as f:
        geojson_data = json.load(f)
    
    features = geojson_data["features"]
    gdf = gpd.GeoDataFrame(
        pd.DataFrame([feature['properties'] for feature in features]),
        geometry=[shape(feature['geometry']) for feature in features],
        crs=crs
    )
    return gdf

