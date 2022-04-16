import time

from django.db import connection, reset_queries


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


def print_queries(func):
    def func_wrapper(*args, **kwargs):
        reset_queries()
        result = func(*args, **kwargs)
        print("Executed queries")
        for query in connection.queries:
            print(query["sql"])

        return result

    return func_wrapper
