#!/usr/bin/env python
import can
from can.bus import BusState

"""
Shows how to receive messages via polling.
"""

def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""

    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.interface.Bus(bustype='serial', channel='/dev/ttyACM0', bitrate=115200) as bus:
        # set to read-only, only supported on some interfaces
        try:
            bus.state = BusState.PASSIVE
        except NotImplementedError:
            pass

        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg)

        except KeyboardInterrupt:
            pass  # exit normally


if __name__ == "__main__":
    receive_all()