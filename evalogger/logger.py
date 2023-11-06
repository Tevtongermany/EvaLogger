from .color import Colors
from aiohttp import ClientResponse
import requests
import datetime
import logging


class EvaLogger:
    _instances = {}

    def __new__(cls, name: str = "default", filename: str = "eva.__log", print_to_console: bool = True,
                save_to_file: bool = False):
        if name not in cls._instances:  # check if the instance exists
            instance = super(EvaLogger, cls).__new__(cls)  # create the instance
            instance.save_to_file = save_to_file  # set the save_to_file attribute
            instance.file_name = filename  # set the file_name attribute
            instance.print_to_console = print_to_console  # set the print_to_console attribute
            cls._instances[name] = instance  # save the instance
        return cls._instances[name]  # return the instance

    # It is just the Get__logger thingie from the __logging module but not so complicated

    def warn(self, text: str):
        if self.print_to_console:
            print(f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.YELLOW}WARN{Colors.RESET}] {text}")
        self.__log("WARN", text)

    def error(self, text: str):
        if self.print_to_console:
            print(f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.RED}ERROR{Colors.RESET}] {text}")
        self.__log("ERROR", text)

    def exception_error(self, exception: Exception):
        if self.print_to_console:
            print(f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.RED}ERROR{Colors.RESET}] {exception.__class__.__name__}: {str(exception)}")
        self.__log("ERROR", f"{exception.__class__.__name__}: {str(exception)}")

    def info(self, text: str):
        if self.print_to_console:
            print(f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.BLUE}INFO{Colors.RESET}] {text}")
        self.__log("INFO", text)

    def success(self, text: str):
        if self.print_to_console:
            print(f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.GREEN}SUCCESS{Colors.RESET}] {text}")
        self.__log("SUCCESS", text)

    def network(self, response, text: str = ""):
        if isinstance(response, requests.Response):
            text_nocolor = f"[{response.request.method}][{response.status_code}] {response.url} {text}"
            print(
                f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.BLUE}NETWORK{Colors.RESET}][{Colors.TURKIS}{response.request.method}{Colors.RESET}][{Colors.MAGENTA}{response.status_code}{Colors.RESET}] {response.url} {text}")
            self.__log("NETWORK", text_nocolor)
        elif isinstance(response, ClientResponse):
            text_nocolor = f"[{response.method}][{response.status}] {response.url} {text}"
            print(
                f"[{str(datetime.datetime.now()).split('.')[0]}][{Colors.BLUE}NETWORK{Colors.RESET}][{Colors.TURKIS}{response.method}{Colors.RESET}][{Colors.MAGENTA}{response.status}{Colors.RESET}] {response.url} {text}")
            self.__log("NETWORK", text_nocolor)

    def __log(self, type: str, text: str):
        if self.save_to_file:
            with open(self.file_name, "a+") as f:
                f.write(f"[{str(datetime.datetime.now()).split('.')[0]}][{type}] {text}\n")
