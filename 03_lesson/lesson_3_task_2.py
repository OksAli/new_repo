from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Redmi S2", "+79998887766"),
    Smartphone("Poco", "M4", "+79069887575"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79089223366"),
    Smartphone("Tecno", "Pova 7", "+79039334455"),
    Smartphone("HONOR", "Magic 7 Pro", "+79012223366")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - {smartphone.subscriber_number}")