def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global B
    B += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(15)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

B = 0
basic.show_string("Nouran ")