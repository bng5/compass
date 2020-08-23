def on_button_pressed_a():
    global brightness
    if brightness > 15:
        brightness += -16
        serial.write_line("" + str((brightness)))
        led.set_brightness(brightness)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global brightness
    if brightness < 255:
        brightness += 16
        serial.write_line("" + str((brightness)))
        led.set_brightness(brightness)
input.on_button_pressed(Button.B, on_button_pressed_b)

degrees = 0
brightness = 255

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    elif degrees < 315:
        basic.show_string("W")
    else:
        basic.show_string("N")
basic.forever(on_forever)
