import requests
latlng_list = [
    [21.186461, 72.808128],
    [28.657291, 77.22726],
    [30.33347, -81.470448],
    [41.947259, -87.65438],
    [38.892062, -77.019912],
    ]
url = "https://www.mapquestapi.com/geocoding/v1/reverse"
key = "dTnNUsIGLsnAKxfMAGulGSLpvGZ4eGsC"
parameter = {"key": key, "location": lat_long[0] + ", " + lat_long[1]}