import numpy as np
import pandas as pd
from lxml import etree

trkpt_tag = '{http://www.topografix.com/GPX/1/1}trkpt'


def elem_to_dict(elem):
    return {
        'lat': float(elem.get('lat')),
        'lng': float(elem.get('lon')),
        'height': float(elem.getchildren()[0].text),
    }


def load_gpx(gpx_file: str) -> pd.DataFrame:
    """Load data from GPX file to a dataframe with lat, lng, height."""
    with open(gpx_file) as fp:
        tree = etree.parse(fp).getroot()

    elems = tree.findall(f'.//{trkpt_tag}')
    return pd.DataFrame.from_records(elem_to_dict(e) for e in elems)


lat_km, lng_km = 92, 111


def distance(lat1, lng1, lat2, lng2):
    """Distance between two points in km."""
    delta_lat = (lat1 - lat2) * lat_km
    delta_lng = (lng1 - lng2) * lng_km
    return np.hypot(delta_lat, delta_lng)


def total_distance(df: pd.DataFrame) -> np.float64:
    """Total distance of a path in km."""
    dist_km = distance(
        df['lat'], df['lng'],
        df['lat'].shift(), df['lng'].shift(),
    )

    return dist_km.sum()
