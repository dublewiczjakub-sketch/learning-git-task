# Program: lista zakupów
zakupy = {
     "piekarnia": ["chleb", "bułki", "pączek", "zapiekanka"],
     "warzywniak": ["marchew", "seler", "rukola","pomidor", "ziemniak"],
     "kosmetyczny": ["szampon", "żel"]
 }
total_products = 0

for shop, products in zakupy.items():
    shop_cap = shop.capitalize()
    products_cap = [product.capitalize() for product in products]
    print(f"Idę do {shop_cap} i kupuję tam {', '.join(products_cap)}.")
    total_products += len(products)

print(f"\nW sumie kupuję {total_products} produktów.")