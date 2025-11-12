# Program: lista zakupów
zakupy = {
     "piekarnia": ["chleb", "bułki", "pączek"],
     "warzywniak": ["marchew", "seler", "rukola"]
 }
for shop, products in zakupy.items():
    print(f"Idę do {shop} i kupuję tam {', '.join(products)}.")