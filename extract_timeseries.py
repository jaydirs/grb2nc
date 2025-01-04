# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:44:20 2025
This script allows me to extract a time series for the given index and
all variables using multiple nc files as source
@author: Jassy Rivera - DACIA
"""
# %%
import xarray as xr
import pandas as pd
from datetime import datetime
import cftime
from netCDF4 import Dataset
# %%
# %% Lectura de archivos
# Índices para el punto más cercano
min_idx=(25,15)

# Rutas a los archivos NetCDF
hs_nc = "C:/Users/Jassy-DACIA/Documents/Erosion costera/Codes/hs_subset.nc"
dp_nc = "C:/Users/Jassy-DACIA/Documents/Erosion costera/Codes/dp_subset.nc"
tp_nc = "C:/Users/Jassy-DACIA/Documents/Erosion costera/Codes/tp_subset.nc"
wind_nc = "C:/Users/Jassy-DACIA/Documents/Erosion costera/Codes/wind_subset.nc"

# Cargar archivos NetCDF
hs = xr.open_dataset(hs_nc)
dp = xr.open_dataset(dp_nc)
tp = xr.open_dataset(tp_nc)
wind = xr.open_dataset(wind_nc)

# Inspeccionar variables
#variables = list(wind.variables.keys())

# Nombrando las variables
swh=hs['swh']
dirpw=dp['dirpw']
perpw=tp['perpw']
ugrd=wind['u']
vgrd=wind['v']
#time=hs['time']
# %%
# Extraer la serie de tiempo para el punto más cercano
swh_ts = swh.isel(lon=min_idx[1], lat=min_idx[0]).values
dirpw_ts = dirpw.isel(lon=min_idx[1], lat=min_idx[0]).values
perpw_ts = perpw.isel(lon=min_idx[1], lat=min_idx[0]).values
ugrd_ts = ugrd.isel(lon=min_idx[1], lat=min_idx[0]).values
vgrd_ts = vgrd.isel(lon=min_idx[1], lat=min_idx[0]).values
# %% 
# Para manejo de las fechas
hs_data = Dataset(hs_nc, mode='r')

# Convertir el tiempo a formato datetime
time_values = hs_data.variables['time'][:]
time_units = hs_data.variables['time'].units

# Usar cftime para convertir las horas a fecha estándar
# cftime.num2date convierte el tiempo basado en un sistema de tiempo "hours since"
fechas_cftime = cftime.num2date(time_values, units=time_units)

# Convertir las fechas cftime a objetos datetime de Python
fechas_python = [datetime(year=date.year, month=date.month, day=date.day,
                          hour=date.hour, minute=date.minute, second=date.second) 
                 for date in fechas_cftime]

# Convertir las fechas datetime a un DataFrame de Pandas
fechas = pd.to_datetime(fechas_python)

# Verificamos si las fechas fueron correctamente convertidas
# print(fechas[:5])  # Muestra las primeras 5 fechas
# %% 
# Crear un DataFrame con tiempo y serie de datos
df = pd.DataFrame({
    "time": fechas,
    "swh": swh_ts,
    "dirpw": dirpw_ts,
    "perpw": perpw_ts,
    "u": ugrd_ts,
    "v": vgrd_ts,
})
# %%
# Guardar como CSV
df.to_csv("C:/Users/Jassy-DACIA/Documents/Erosion costera/Codes/serie_de_tiempo.csv", index=False)
print("Serie de tiempo guardada como 'serie_de_tiempo.csv'")

