from db.seed_data import generate_tenants, generate_payments, generate_properties, generate_rental_units, \
    generate_rental_contracts, generate_maintenance_requests
from db.connection import test_db_connection
from config.variables import DB_ENTRIES

db = test_db_connection()


def main():
    print(f"🔢 Anzahl der Einträge: {DB_ENTRIES}")
    print("Daten werden importiert...")

    tenants = generate_tenants(DB_ENTRIES)
    tenant_ids = db.tenants.insert_many(tenants).inserted_ids
    print(f"{len(tenant_ids)} Mieter eingefügt.")

    properties = generate_properties(DB_ENTRIES)
    property_ids = db.properties.insert_many(properties).inserted_ids
    print(f"{len(property_ids)} Liegenschaften eingefügt.")

    rental_units = generate_rental_units(DB_ENTRIES, tenant_ids, property_ids)
    rental_unit_ids = db.rental_units.insert_many(rental_units).inserted_ids
    print(f"{len(rental_unit_ids)} Mietobjekte eingefügt.")

    contracts = generate_rental_contracts(DB_ENTRIES, tenant_ids, rental_unit_ids)
    contract_ids = db.rental_contracts.insert_many(contracts).inserted_ids
    print(f"{len(contract_ids)} Mietverträge eingefügt.")

    payments = generate_payments(DB_ENTRIES, contract_ids)
    db.payments.insert_many(payments)
    print(f"{DB_ENTRIES} Zahlungen eingefügt.")

    maintenance = generate_maintenance_requests(DB_ENTRIES, rental_unit_ids)
    db.maintenance_requests.insert_many(maintenance)
    print(f"{DB_ENTRIES} Wartungsanfragen eingefügt.")


if __name__ == "__main__":
    main()
