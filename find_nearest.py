# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:24:17 2025
This script finds the coordinates and index for the nearest point
to my desired location considering only not NaN values (sea values)
@author: Jassy Rivera - DACIA
"""
import numpy as np
import xarray as xr

# Cargar archivo NetCDF
filename = "hs_subset.nc"
ds = xr.open_dataset(filename)
#variables = list(ds.variables.keys())
#print(variables)

# Extraer datos relevantes
lons = ds["lon"].values  # Longitudes
lats = ds["lat"].values  # Latitudes
swh = ds["swh"]          # Altura significativa de olas

# Convertir _FillValue a NaN
fill_value = swh.attrs.get("_FillValue", None)
swh = swh.where(swh != fill_value)  # Convertir _FillValue a NaN

# Crear grillas 2D de latitud y longitud
lon2d, lat2d = np.meshgrid(lons, lats)

# Máscara de valores válidos (en el mar)
valid_mask = ~np.isnan(swh.isel(time=1).values)  # Tomamos el primer tiempo como ejemplo

# Coordenadas objetivo
target_lat = 12.34  # Cambiar por tu latitud objetivo
target_lon = 272.35  # Cambiar por tu longitud objetivo

# Calcular la distancia para cada punto en la grilla
distances = np.sqrt((lat2d - target_lat)**2 + (lon2d - target_lon)**2)

# Enmascarar el array de distancias usando la máscara de puntos válidos
masked_distances = np.where(valid_mask, distances, np.inf)

# Encontrar el índice del punto válido más cercano
min_idx = np.unravel_index(np.argmin(masked_distances), masked_distances.shape)

# Extraer el valor de la máscara para el punto más cercano
mask_value = valid_mask[min_idx]

# Obtener las coordenadas del punto más cercano
closest_lat = lat2d[min_idx]
closest_lon = lon2d[min_idx]

print(f"El punto más cercano válido está en: ({closest_lat}, {closest_lon})")
print(f"Distancia al punto objetivo: {masked_distances[min_idx]}")
print(f"Índices del punto más cercano: {min_idx}")

