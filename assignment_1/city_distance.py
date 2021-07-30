from math import radians, cos, sin, asin, sqrt


def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    d = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    dis = 2 * asin(sqrt(d))
    rad = 6371
    return (dis * rad)


city1 = input("City 1: ")
city2 = input("City 2: ")

c1 = city1.split(", ")
c2 = city2.split(", ")

lat1 = float(c1[0].split()[0])
lon1 = float(c1[1].split()[0])
lat2 = float(c2[0].split()[0])
lon2 = float(c2[1].split()[0])

dist = round(distance(lat1, lat2, lon1, lon2), 2)



print("Output: City 1 and City 2 are " + str(dist) + " km apart")