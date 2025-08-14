from address import Address
from mailing import Mailing

to_address = Address("358014", "Элиста", "9мкр", "21", "124")
from_address = Address("142721", "Видное", "Молодежный бульвар", "14", "122")

mailing = Mailing(to_address, from_address, 200, 68901165)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.building} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.building} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
