import inputs

def get_xbox_controller_input():
    events = inputs.get_gamepad()
    for event in events:
        # Xbox controller event codes
        if event.ev_type == "Absolute":
            if event.code == "ABS_X":
                print("Left joystick X-axis:", event.state)
            elif event.code == "ABS_Y":
                print("Left joystick Y-axis:", event.state)
            elif event.code == "ABS_RX":
                print("Right joystick X-axis:", event.state)
            elif event.code == "ABS_RY":
                print("Right joystick Y-axis:", event.state)
            elif event.code == "ABS_Z":
                print("Left trigger:", event.state)
            elif event.code == "ABS_RZ":
                print("Right trigger:", event.state)
        elif event.ev_type == "Key":
            if event.code == "BTN_SOUTH":
                print("A button pressed")
            elif event.code == "BTN_EAST":
                print("B button pressed")
            elif event.code == "BTN_NORTH":
                print("Y button pressed")
            elif event.code == "BTN_WEST":
                print("X button pressed")
            # Add more button codes as needed

# Main loop
while True:
    get_xbox_controller_input()
