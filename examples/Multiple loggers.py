from evalogger import EvaLogger

log_1 = EvaLogger(name="eva1", save_to_file=True, filename="eva1.log")

log_2 = EvaLogger(name="eva2", save_to_file=False)

log_1.info("Hello World!")  # log a info message to eva1.log

log_2.info("Hello World!")  # log a info message to stdout