import random as rd
import questionary


class Server:

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.status = 'ONLINE'
        self.cpu_usage = 20

    def wlacz(self):
        self.status = 'ONLINE'
        self.cpu_usage = 20

    def wylacz(self):
        self.status = 'OFFLINE'
        self.cpu_usage = 0

    def wyswietl_info(self):
        return f"[{self.status}] {self.name} ({self.ip}) - CPU: {self.cpu_usage}%"

    def nazwa(self):
        return self.name


infrastruktura = [
    Server("auth-db", "10.0.0.10"),
    Server("web-frontend", "10.0.0.11"),
    Server("payment-gateway", "10.0.0.12")
]


def wyswietl_status():
    print("\n=== STATUS INFRASTRUKTURY ===")

    for serwer in infrastruktura:
        print(serwer.wyswietl_info())

    print()


def wybierz_serwer():

    nazwy = [s.name for s in infrastruktura]

    wybor = questionary.select(
        "Wybierz serwer:",
        choices=nazwy
    ).ask()

    return next((s for s in infrastruktura if s.name == wybor), None)


def zmien_status():

    serwer = wybierz_serwer()

    if not serwer:
        return

    akcja = questionary.select(
        f"Co chcesz zrobić z serwerem {serwer.name}?",
        choices=[
            "wlacz",
            "wylacz",
            "anuluj"
        ]
    ).ask()

    if akcja == "wlacz":
        serwer.wlacz()
        print(f"\nSerwer {serwer.name} został włączony.\n")

    elif akcja == "wylacz":
        serwer.wylacz()
        print(f"\nSerwer {serwer.name} został wyłączony.\n")

    else:
        print("\nAnulowano operację.\n")


def symuluj_obciazenie():

    print("\n=== SYMULACJA OBCIĄŻENIA ===")

    for serwer in infrastruktura:

        if serwer.status == "OFFLINE":
            serwer.cpu_usage = 0
            print(f"{serwer.name} -> OFFLINE | CPU 0%")
            continue

        los = rd.randint(10, 100)

        serwer.cpu_usage = los

        print(f"{serwer.name} -> CPU {los}%")

        if los > 90:
            print(f"[ALERT] Serwer {serwer.name} jest przeciążony!")

    print()


while True:

    wybor = questionary.select(
        "Wybierz opcję z menu:",
        choices=[
            "Wyswietl status infrastruktury",
            "Zmien stan serwera",
            "Symuluj losowe obciazenie",
            "Koniec programu"
        ]
    ).ask()

    if wybor == "Wyswietl status infrastruktury":
        wyswietl_status()

    elif wybor == "Zmien stan serwera":
        zmien_status()

    elif wybor == "Symuluj losowe obciazenie":
        symuluj_obciazenie()

    elif wybor == "Koniec programu":
        print("\nZamykanie programu...")
        break
