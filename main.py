def find_coupe(place_number):
    coupe = (place_number - 1) // 4 + 1 # Возвращаем номер купе return coupe
    return coupe
place_number = int(input())
print(find_coupe(place_number))