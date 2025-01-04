#!usr/bin/sh
cd ./wind/Vgrd
mkdir subsets
for file in *.grb2; do
    echo "Procesando $file"
    cdo sellonlatbox,265,285,5,25 "$file" "subsets/${file%.grb2}_clip.grb2"
done