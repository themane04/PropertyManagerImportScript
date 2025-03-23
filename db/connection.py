import pymongo
from config.variables import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


def test_db_connection():
    try:
        client = pymongo.MongoClient(f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?authSource=admin")
        db = client[DB_NAME]
        db.command("ping")
        print("✅ Verbindung zur MongoDB erfolgreich!")
        return db
    except Exception as e:
        print(f"❌ Fehler bei der Verbindung: {e}")
        return None


if __name__ == "__main__":
    test_db_connection()
