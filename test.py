from typing import List

def double_numbers(numbers: List[int]) -> List[int]:
    """
    Aldığı sayı listesinin her bir elemanını iki katına çıkaran bir fonksiyon.
    """
    # Sadece tamsayıları işle, diğer türleri ignore et
    doubled = [num * 2 if isinstance(num, int) else num for num in numbers]
    return doubled

# Test etmek için bir liste oluşturalım
numbers = [1, 2, "three", 4, 5]  # "three" dize elemanı tamsayı değil

# Fonksiyonu çağırıp sonucu alalım
doubled_numbers = double_numbers(numbers)

# Sonucu yazdıralım
print("Orijinal Liste:", numbers)
print("İki Katı:", doubled_numbers)
