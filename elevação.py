import gpxpy

# Abra o arquivo GPX
with open('Só_montanha_desafio_pedal_de_oz.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)

# Inicializa variáveis
total_elevation_gain = 0
last_elevation = None

# Itera pelos pontos da rota
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            if last_elevation is not None and point.elevation > last_elevation:
                total_elevation_gain += point.elevation - last_elevation
            last_elevation = point.elevation

print(f"Ganho total de elevação: {total_elevation_gain:.2f} metros")
