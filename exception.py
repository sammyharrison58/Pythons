from __future__ import annotations

import logging
from typing import NoReturn


class InvalidNumberError(Exception):

    pass


def parse_int(value: str) -> int:

    try:
        return int(value)
    except ValueError as e:
        # Preserve original traceback via exception chaining
        raise InvalidNumberError(f"Invalid integer: {value!r}") from e


def divide_ten_by(divisor: int) -> float:

    return 10 / divisor


def configure_logging() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def main() -> None:

    configure_logging()

    try:
        raw = input("Enter a number: ")
        try:
            number = parse_int(raw)
        except InvalidNumberError:
            logging.exception("Error: Invalid input. Please enter a valid integer.")
            return
        try:
            result = divide_ten_by(number)
        except ZeroDivisionError:
            logging.exception("Error: Division by zero is not allowed.")
            return
        print(f"You entered: {number}")
        print(f"10 divided by {number} is {result}")

    except Exception:

        logging.exception("An unexpected error occurred.")
    finally:
        print("Execution completed.")


if __name__ == "__main__":
    main()
