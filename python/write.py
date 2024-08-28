import can

bus = can.interface.Bus(bustype='serial', channel='/dev/ttyACM0', bitrate=115200)

msg = can.Message(arbitration_id=0xc0ffee, data=[0, 1, 2, 3, 4, 5, 6, 7], is_extended_id=True)

try: 
    bus.send(msg)
    print("Message sent on {}".format(bus.channel_info))
except can.CanError:
    print("Message NOT sent")