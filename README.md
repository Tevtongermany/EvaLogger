# EvaLogger
Eva Logger is a simple logging library for Python. It is designed to be easy to use and to be easily integrated into existing projects.

Usage
-----

```python
from evalogger import EvaLogger
import requests

log = EvaLogger()  # create a EvaLogger instance

log.info("Hello World!")  # log a info message
log.warn("Hello World!")  # log a warning message
log.error("Hello World!") # log a error message
log.exception_error(RuntimeError("Hello World!")) # log a exception error message
log.success("Hello World!")  # log a success message
log.network(requests.get("https://google.com"))  # log a network request
log.network(requests.get("https://google.com"), text="Google")  # log a network request with a custom name

```
Configuration
-------------
EvaLogger doesn't have alot of configuration options, but it does have some.    
You can configure EvaLogger by setting the following properties on the EvaLogger instance.
```python
from evalogger import EvaLogger

log = EvaLogger(save_to_file=True, filename="eva.log")
```
EvaLogger has support for multiple loggers at once.
```python
from evalogger import EvaLogger

log_1 = EvaLogger(name="eva1", save_to_file=True, filename="eva1.log")

log_2 = EvaLogger(name="eva2", save_to_file=False)

log_1.info("Hello World!")  # log a info message to eva1.log

log_2.info("Hello World!")  # log an info message to stdout
```

Example
-------
You can find all examples in the examples folder in the repository.



