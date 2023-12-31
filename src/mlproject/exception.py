import sys
import logging

def error_message_detailed(error):
    _, _, exc_tb = sys.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = error_message_detailed(error)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by Zero")
        raise CustomException(e,sys)
