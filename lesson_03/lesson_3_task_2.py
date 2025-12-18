from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79098765432"))
catalog.append(Smartphone("Xiaomi", "14 Pro", "+79501234567"))
catalog.append(Smartphone("Google", "Pixel 8", "+79987654321"))
catalog.append(Smartphone("OnePlus", "12", "+79876543210"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
