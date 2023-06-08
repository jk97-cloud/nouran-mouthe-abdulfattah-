input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function () {
    B += 1
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(15)
})
let B = 0
basic.showString("Nouran ")
