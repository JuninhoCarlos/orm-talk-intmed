def timed(func):
    def func_wrapper(*args, **kwargs):
        import time

        s = time.perf_counter()
        result = func(*args, **kwargs)
        e = time.perf_counter()
        print("The executions takes %f seconds" % (e - s))
        return result

    return func_wrapper
