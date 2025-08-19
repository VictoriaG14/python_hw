from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "s22ultra", "79996665588"),
    Smartphone("iPhone", "16pro", "79091234545"),
    Smartphone("Xiaomi", "15", "78083331232"),
    Smartphone("Oppo", "A5pro", "79935456611"),
    Smartphone("Honor", "400lite", "79036541230")
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.type}. {Smartphone.number}")
