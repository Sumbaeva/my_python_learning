from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Победы", "5", "30")

my_mailing = Mailing(to_addr, from_addr, 250, "TRACK123456")

print(
    f"Отправление {my_mailing.track} из "
    f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} в {my_mailing.to_address.index}, "
    f"{my_mailing.to_address.city}, {my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - {my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)
