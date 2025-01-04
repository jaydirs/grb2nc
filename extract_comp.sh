#!usr/bin/sh

# Ruta del directorio con los archivos GRB2
input_dir="$(pwd)"
output_diru="/Ugrd"
output_dirv="/Vgrd"

# Crear el directorio de salida si no existe
mkdir -p "$output_diru"
mkdir -p "$output_dirv"

# Iterar sobre todos los archivos .grb2 en el directorio
for file in "$input_dir"/*.grb2; do
    # Obtener el nombre base del archivo sin extensión
    base_name=$(basename "$file" .grb2)
    
    echo "Procesando archivo: $file"
    
    # Extraer la componente UGRD
    wgrib2 "$file" -match "UGRD" -grib "$output_diru/${base_name}_UGRD.grb2"
    
    # Extraer la componente VGRD
    wgrib2 "$file" -match "VGRD" -grib "$output_dirv/${base_name}_VGRD.grb2"
done

echo "Procesamiento finalizado. Archivos guardados en $output_dir"
