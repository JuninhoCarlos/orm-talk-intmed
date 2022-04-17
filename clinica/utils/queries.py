import time

from django.db import connection


class CountQueries:
    """
    This class is used to count the number of queries executed inside the context.
    """

    def __enter__(self):
        self.count = len(connection.queries)
        return self

    def __exit__(self, *args, **kwargs):
        res = len(connection.queries) - self.count
        print("Number of queries: ", res)
