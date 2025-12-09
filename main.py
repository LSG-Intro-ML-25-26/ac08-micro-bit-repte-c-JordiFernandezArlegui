def on_button_pressed_a():
    radio.send_string("" + str((String2)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)

String2 = 0
String2 = 0