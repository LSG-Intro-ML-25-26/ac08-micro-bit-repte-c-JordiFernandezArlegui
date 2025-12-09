num = 0
String2 = ""

def on_received_number(receivedNumber):
    if num > 3:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global String2
    String2 = "String"
    radio.send_string(String2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(String2)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global num
    num += randint(1, 6)
    radio.send_number(num)
input.on_button_pressed(Button.B, on_button_pressed_b)
