#!usr/bin/sh
abase=2006
prefijo=https://polar.ncep.noaa.gov/waves/hindcasts/nopp-phase2/
sufijo=/gribs/multi_reanal.glo_30m_ext
variable=.wind.
extension=.grb2
for i in {1..3}
 do 
	let anio=abase+i
	echo $anio
	for j in {01..12}
		do
		mes=$j
		wget -P ./wind $prefijo$anio$mes$sufijo$variable$anio$mes$extension
		done
 done
#download.sh
#url=$(awk -F = '{print $2}' url.txt)
#for i in $(cat file.txt);
#do 
#wget $url
#done
#wget "${url}${i}"
#wget -P ./dp https://polar.ncep.noaa.gov/waves/hindcasts/nopp-phase2/200612/gribs/multi_reanal.glo_30m_ext.dp.200612.grb2
#wget -P ./tp https://polar.ncep.noaa.gov/waves/hindcasts/nopp-phase2/199512/gribs/multi_reanal.glo_30m_ext.tp.199512.grb2
wget -P ./hs https://polar.ncep.noaa.gov/waves/hindcasts/nopp-phase2/200909/gribs/multi_reanal.glo_30m_ext.tp.200909.grb2
#Para mover archivos
# mv ruta_actual/carpeta ruta_nueva/carpeta