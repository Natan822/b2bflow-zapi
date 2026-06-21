from supabase import create_client
from supabase import SupabaseException

class DBClient:
    def __init__(self, url: str, key: str):
        try:
            self.client = create_client(url, key)
        except SupabaseException as e:
            raise RuntimeError(f"Failed to initialize Supabase client: {e}") from e

    def insert(self, table: str, data: dict):
        try:
            return self.client.table(table).insert(data).execute().data
        except SupabaseException as e:
            raise RuntimeError(f"Failed to insert into '{table}': {e}") from e

    def get_by_id(self, table: str, record_id, id_column: str = "id"):
        try:
            result = (
                self.client.table(table)
                .select("*")
                .eq(id_column, record_id)
                .limit(1)
                .execute()
            )

            return result.data[0] if result.data else None
        except SupabaseException as e:
            raise RuntimeError(f"Failed to get record from '{table}' where {id_column}={record_id}: {e}") from e

    def find(self, table: str, filters: dict | None = None, columns: str = "*"):
        try:
            query = self.client.table(table).select(columns)

            if filters:
                for key, value in filters.items():
                    query = query.eq(key, value)

            return query.execute().data
        except SupabaseException as e:
            raise RuntimeError(f"Failed to query '{table}': {e}") from e

    def all(self, table: str, columns: str = "*"):
        try:
            return self.client.table(table).select(columns).execute().data
        except SupabaseException as e:
            raise RuntimeError(f"Failed to fetch all records from '{table}': {e}") from e

    def update(self, table: str, record_id, data: dict, id_column: str = "id"):
        try:
            return (
                self.client.table(table)
                .update(data)
                .eq(id_column, record_id)
                .execute()
                .data
            )
        except SupabaseException as e:
            raise RuntimeError(f"Failed to update record in '{table}' where {id_column}={record_id}: {e}") from e

    def delete(self, table: str, record_id, id_column: str = "id"):
        try:
            return (
                self.client.table(table)
                .delete()
                .eq(id_column, record_id)
                .execute()
                .data
            )
        except SupabaseException as e:
            raise RuntimeError(f"Failed to delete record from '{table}' where {id_column}={record_id}: {e}") from e

    def rpc(self, function_name: str, params: dict | None = None):
        try:
            return self.client.rpc(function_name, params or {}).execute().data
        except SupabaseException as e:
            raise RuntimeError(f"Failed to execute RPC '{function_name}': {e}") from e

    def table(self, table: str):
        try:
            return self.client.table(table)
        except SupabaseException as e:
            raise RuntimeError(f"Failed to access table '{table}': {e}") from e