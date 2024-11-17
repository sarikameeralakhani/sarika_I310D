from math import pi

def calculate_volume_of_sphere(radius):
  volume = (4/3) * pi * (radius ** 3)
  return volume

radius1 = 30
radius2 = 40
volume1 = calculate_volume_of_sphere(radius1)
volume2 = calculate_volume_of_sphere(radius2)

print(f"Radius: {radius1}. Volume: {volume1}")   

print(f"Radius: {radius2}. Volume: {volume2}")
