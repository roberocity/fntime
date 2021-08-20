
fntime provides a simple method for calculating how many times a
function can be executing within a number of seconds.

This is intented to test functions that already execute quickly. 

The method under test will be run at least twice. The first run
is before the time interval start. Once the time interval starts the
function will be run until the time period expires. 

Install the library

```bash
$ pip install fntime
```

Use the library

```python
from fntime import time_function

def mult(a, b):
    return a * b

execution_count, name, run_time, result = time_function(1.5, mult, 4, 5)

# or

result = time_function(1.5, mult, 4, 5)
```

Override the method name property

```python
from fntime import time_function

fn = lambda a, b: a * b

execution_count, name, _, _ = time_function(3, fn, 4, 5)
# name == <lambda>

execution_count, name, _, _ = time_function(3, fn, 4, 5, method_name='mult lambda')
# name == 'mult lambda'
```

The value returned in run_time will be the actual time that the executions took.
The function will always be run once during the timed portion. 

