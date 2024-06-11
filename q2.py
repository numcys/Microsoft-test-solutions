from functools import wraps
import time

def execution_time(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    execution_time = time.time() - start_time
    print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
    return result
  return wrapper

@execution_time
def some_function(a, b):
  time.sleep(1)  
  return a * b

result = some_function(5, 3)
