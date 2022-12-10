from ways import load_map_from_csv
from math import acos, radians, pi
from  numpy import cos, sin

roads = load_map_from_csv()


def compute_distance(lat1, lon1, lat2, lon2):
    '''computes distance in KM'''
    '''
    This code was borrowed from 
    http://www.johndcook.com/python_longitude_latitude.html
    '''
    if (lat1, lon1) == (lat2, lon2):
        return 0.0
    if max(abs(lat1 - lat2), abs(lon1 - lon2)) < 0.00001:
        return 0.001

    phi1 = radians(90 - lat1)
    phi2 = radians(90 - lat2)

    meter_units_factor = 40000 / (2 * pi)
    arc = acos(sin(phi1) * sin(phi2) * cos(radians(lon1) - radians(lon2))
               + cos(phi1) * cos(phi2))
    return arc * meter_units_factor
