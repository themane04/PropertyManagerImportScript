import random
from datetime import datetime, timedelta

from faker import Faker

fake = Faker()


def generate_tenants(n):
    return [{
        "vorname": fake.first_name(),
        "nachname": fake.last_name(),
        "geburtsdatum": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
        "email": fake.email(),
        "telefonnummer": fake.phone_number(),
        "adresse": {
            "strasse": fake.street_name(),
            "hausnummer": str(random.randint(1, 200)),
            "plz": str(random.randint(1000, 9999)),
            "stadt": fake.city()
        },
        "mietverträge": []
    } for _ in range(n)]


def generate_properties(n):
    return [{
        "name": f"{fake.last_name()} Wohnanlage",
        "adresse": {
            "strasse": fake.street_name(),
            "hausnummer": str(random.randint(1, 100)),
            "plz": str(random.randint(1000, 9999)),
            "stadt": fake.city()
        },
        "baujahr": random.randint(1950, 2023),
        "anzahl_wohnungen": random.randint(5, 50),
        "anzahl_parkplätze": random.randint(2, 20),
        "besitzer": fake.company(),
        "mietobjekte": []
    } for _ in range(n)]


def generate_rental_units(n, tenant_ids, property_ids):
    return [{
        "bezeichnung": f"Wohnung {fake.random_uppercase_letter()}{random.randint(1, 30)}",
        "typ": random.choice(["Wohnung", "Büro", "Laden", "Penthouse"]),
        "fläche_m2": random.randint(40, 250),
        "zimmeranzahl": random.randint(1, 6),
        "miete": random.randint(800, 8000),
        "verfügbar_ab": datetime.combine(fake.date_between("today", "+6M"), datetime.min.time()),
        "status": random.choice(["vermietet", "frei"]),
        "mieter_id": random.choice(tenant_ids),
        "liegenschaft_id": random.choice(property_ids),
        "ausstattungen": random.sample(["Balkon", "Küche", "Parkplatz", "Tiefgarage", "Jacuzzi"],
                                       k=random.randint(1, 3))
    } for _ in range(n)]


def generate_rental_contracts(n, tenant_ids, rental_unit_ids):
    contracts = []
    for _ in range(n):
        start = fake.date_between('-2y', 'today')
        end = start + timedelta(days=random.randint(365, 1095))
        contracts.append({
            "mieter_id": random.choice(tenant_ids),
            "mietobjekt_id": random.choice(rental_unit_ids),
            "vertragsbeginn": datetime.combine(start, datetime.min.time()),
            "vertragsende": datetime.combine(end, datetime.min.time()),
            "mietzins": random.randint(900, 7500),
            "kaution": random.randint(1000, 15000),
            "status": random.choice(["aktiv", "beendet"])
        })
    return contracts


def generate_payments(n, contract_ids):
    return [{
        "mietvertrag_id": random.choice(contract_ids),
        "datum": datetime.combine(fake.date_between('-6M', 'today'), datetime.min.time()),
        "betrag": random.randint(900, 7500),
        "status": random.choice(["bezahlt", "offen", "fehlgeschlagen"]),
        "zahlungsart": random.choice(["Banküberweisung", "Kreditkarte", "PayPal", "Lastschrift"])
    } for _ in range(n)]


def generate_maintenance_requests(n, rental_unit_ids):
    return [{
        "mietobjekt_id": random.choice(rental_unit_ids),
        "beschreibung": random.choice(
            ["Heizung defekt", "Wasserleck", "Licht flackert", "Fenster undicht", "Tür klemmt"]),
        "status": random.choice(["offen", "in Bearbeitung", "erledigt", "dringend"]),
        "erstellt_am": datetime.combine(fake.date_between("-3M", "today"), datetime.min.time()),
        "zugewiesener_handwerker": fake.company()
    } for _ in range(n)]
