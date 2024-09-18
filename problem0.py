def fibonacci(num, memo=None, trace_calls=None):
    if memo is None:
        memo = {}
    if trace_calls is None:
        trace_calls = []

    # Record the function call
    trace_calls.append(f'fibonacci({num})')

    if num in memo:
        return memo[num]

    if num == 0:
        return 0
    if num == 1:
        return 1

    # Compute the result while tracing
    memo[num] = fibonacci(num - 1, memo, trace_calls) + fibonacci(num - 2, memo, trace_calls)
    return memo[num]

# Wrapper function to start debugging
def fibonacci_debug(num):
    trace_calls = []
    final_result = fibonacci(num, trace_calls=trace_calls)
    return trace_calls, final_result

# Run the debug function
trace_calls, final_result = fibonacci_debug(5)
print("Trace of Calls:", " -> ".join(trace_calls))
print("Final Result:", final_result)
