import logging

# verbose -> logging.INFO
# debug -> logging.DEBUG

logging.basicConfig(
    filename="numpairs.log",
    level=logging.DEBUG,
)

numpairs = [(5, 1), (1, 5), (5, 0), (0, 5), (17, 0), (9, 5), (85, 0), (1, 2)]

total = 0

logging.info("program starting")

for x, y in numpairs:
    try:
        quotient = x / y
    except ZeroDivisionError as err:
        # print(f"{err}: x = {x} y = {y}")
        logging.exception("Invalid numbers: x is %s y is %s", x, y)  # equal to logging.error()
    else: # if no exceptions were raised
        total += quotient  # Only if no exceptions were raised
    finally:  # no matter what
        # cleanup!
        print("oh heck")

print(total)
