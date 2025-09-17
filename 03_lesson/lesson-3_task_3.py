from Mailing import Mailing
from address import Address

to_adress = Address("353417","Anapa","Chuiko", "1", "10")
from_adress = Address("354000", "Sochi", "Bam", "4", "5")

mailing = Mailing(to_adress, from_adress, 500, "4564561223")
                   
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)