from db_client import DBClient
from zapi_client import ZAPIClient

import os
import logging

logging.basicConfig(level=logging.INFO)

def print_users_table(table: list[dict]):
    print("ID Name Number")
    for user in table:
        print(f"{user["id"]}: {user.get("name", "")} {user.get("number", "")}")

def main():
    SUPA_URL = os.getenv("SUPABASE_URL")
    SUPA_KEY = os.getenv("SUPABASE_KEY")

    ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    ZAPI_INSTANCE_TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
    ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

    db = DBClient(SUPA_URL, SUPA_KEY)
    zapi = ZAPIClient(ZAPI_INSTANCE_ID, ZAPI_INSTANCE_TOKEN, ZAPI_CLIENT_TOKEN)
    
    users = db.all("users")
    print_users_table(users)
    
    ids = input("Digite os ID's dos usuários a serem contatados separados por um espaço (Ex.: 12 100 30):").split(" ")
    for id in ids:
        try:
            id = int(id)
        except ValueError:
            print(f"Formato de ID inválido: {id}")
            continue

        user = next((u for u in users if u["id"] == id), None)
        if not user:
            print(f"ID inválido: {id}")
            continue
        
        phone = user.get("number", None)
        if not phone:
            print(f"Número não cadastrado para ID {id}")
            continue

        name = user.get("name", None)
        if not name:
            print(f"Nome não cadastrado para ID {id}")
            continue

        message = ZAPIClient.get_default_message(name)
        zapi.send_message(phone, message)

if __name__ == '__main__':
    main()