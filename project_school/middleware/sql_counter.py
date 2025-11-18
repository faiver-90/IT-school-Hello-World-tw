from django.db import connection
from django.utils.deprecation import MiddlewareMixin
import time


class QueryCountMiddleware(MiddlewareMixin):
    """
    Middleware для подсчёта количества SQL-запросов за обработку одного HTTP-запроса.
    Показывает:
    - количество запросов
    - общее время выполнения SQL
    """

    def process_request(self, request):
        # Время старта запроса
        request._query_start_time = time.time()

        # Сбрасываем лог запросов
        connection.queries_log.clear()

    def process_response(self, request, response):
        # Сколько SQL запросов было выполнено
        query_count = len(connection.queries)

        # Общая длительность SQL
        total_sql_time = sum(float(q["time"]) for q in connection.queries)

        print("\n" + "-" * 40)
        print(f"Path: {request.path}")
        print(f"SQL Queries: {query_count}")
        print(f"Total SQL time: {total_sql_time:.6f} sec")
        print("-" * 40 + "\n")

        return response
