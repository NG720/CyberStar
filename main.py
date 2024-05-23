import math

# Noktaları temsil eden demetlerin (tuple) listesi
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid mesafesi hesaplamak için bir fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Her bir nokta çifti arasındaki Öklid mesafesini hesaplamak
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

print("Minimum mesafe:", min_distance)
