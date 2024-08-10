def yuqori_narx(limit, data):
    sorted_data = sorted(data, key=lambda x: x["price"], reverse=True)
    return sorted_data[:limit]
n = int(input("Mahsulotlar sonini kiriting: "))
products = []
for i in range(n):
    name = input(f"{i+1}-mahsulotning nomini kiriting: ")
    price = int(input(f"{i+1}-mahsulotning narxini kiriting: "))
    products.append({"name": name, "price": price})

limit = int(input("Nechta eng qimmat mahsulotni ko'rmoqchisiz? "))

result = yuqori_narx(limit, products)

print("Eng qimmat mahsulotlar:")
for item in result:
    print(f"Nomi: {item['name']}, Narxi: {item['price']}")
