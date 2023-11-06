from evalogger import EvaLogger
import requests

log = EvaLogger()  # create a EvaLogger instance

log.info("Hello World!")  # log a info message
log.warn("Hello World!")  # log a warning message
log.error("Hello World!")  # log a error message
log.exception_error(RuntimeError("Hello World!"))  # log a exception error message
log.success("Hello World!")  # log a success message
log.network(requests.get("https://google.com"))  # log a network request
log.network(requests.get("https://google.com"), text="Google")  # log a network request with a custom name
