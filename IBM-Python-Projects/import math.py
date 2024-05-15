import math

# Öklid Mesafesi İçin Fonksiyon Tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Programın Çalıştırılması
def main():
    # Kullanıcıdan noktaları al
    points = [(2, 3), (5, 7), (8, 9), (10, 4)]  # Örnek noktalar

    # Minimum Mesafenin Bulunması
    min_distance = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = euclideanDistance(points[i], points[j])
            min_distance = min(min_distance, dist)

    # Sonucu Yazdırma
    print("Noktalar arasındaki minimum Öklid mesafesi:", min_distance)

if __name__ == "__main__":
    main()