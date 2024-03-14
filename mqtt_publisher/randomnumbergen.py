import sys
import time

import publisher as p
from random import randrange, uniform


def generate_temps(receiver):
    topic_in = f"{receiver}/TEMP_IN"
    topic_out = f"{receiver}/TEMP_OUT"
    print("Receiver IN:", topic_in, " Receiver OUT:", topic_out)
    while True:
        temp_in = uniform(20.0, 21.0)
        p.send_out(topic_in, temp_in)
        temp_out = uniform(10.0, 15.0)
        p.send_out(topic_out, temp_out)
        time.sleep(1)


if __name__ == "__main__":
    generate_temps(sys.argv[1])
