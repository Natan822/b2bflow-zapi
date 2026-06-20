from supabase import create_client
from supabase import SupabaseException

class DBClient:
    def __init__(self, url: str, key: str):
        try:
            self.client = create_client(url, key)
        except SupabaseException as e:
            raise RuntimeError(f"Failed to initialize Supabase client: {e}") from e

    def insert(self, table: str, data: dict):
        return self.client.table(table).insert(data).execute().data

    def get_by_id(self, table: str, record_id, id_column: str = "id"):
        result = (
            self.client.table(table)
            .select("*")
            .eq(id_column, record_id)
            .limit(1)
            .execute()
        )

        return result.data[0] if result.data else None

    def find(self, table: str, filters: dict | None = None, columns: str = "*"):
        query = self.client.table(table).select(columns)

        if filters:
            for key, value in filters.items():
                query = query.eq(key, value)

        return query.execute().data

    def all(self, table: str, columns: str = "*"):
        return self.client.table(table).select(columns).execute().data

    def update(self, table: str, record_id, data: dict, id_column: str = "id"):
        return (
            self.client.table(table)
            .update(data)
            .eq(id_column, record_id)
            .execute()
            .data
        )

    def delete(self, table: str, record_id, id_column: str = "id"):
        return (
            self.client.table(table)
            .delete()
            .eq(id_column, record_id)
            .execute()
            .data
        )

    def rpc(self, function_name: str, params: dict | None = None):
        return self.client.rpc(function_name, params or {}).execute().data

    def table(self, table: str):
        return self.client.table(table)
