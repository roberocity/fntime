
def time_function(run_time, fn, *args, method_name=None):
    from time import perf_counter

    """
    Computes the number of times the function can
    be execution within the run_time.

    The name of the function is determined by the 
    fn.__qualname__ property unless the method_name 
    parameter is provided.

    fn is executed once prior to starting the timed run. The
    return value from this run is returned as result.

    Parameters:
        run_time:float - The number of seconds to run 
        fn:function - The function to execute
        args - The arguments to pass into the function
        method_name:str - overrides the name of the function

    Returns:
        execution_count:int, 
        function_name:str, 
        run_time:float, 
        result
    """

    if method_name == None:
        method_name = fn.__qualname__

    start = perf_counter()
    end = start + run_time
    execution_count = 0
    result = None

    result = fn(*args)

    while perf_counter() < end:
        execution_count = execution_count + 1
        fn(*args)

    end = perf_counter()

    return execution_count, method_name, (end - start), result