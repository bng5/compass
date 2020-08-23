input.onButtonPressed(Button.A, function () {
    if (brightness > 15) {
        brightness += -16
        led.setBrightness(brightness)
    }
})
input.onButtonPressed(Button.B, function () {
    if (brightness < 255) {
        brightness += 16
        led.setBrightness(brightness)
    }
})
let degrees = 0
let brightness = 0
brightness = 255
basic.forever(function () {
    degrees = input.compassHeading()
    if (degrees < 45) {
        basic.showString("N")
    } else if (degrees < 135) {
        basic.showString("E")
    } else if (degrees < 225) {
        basic.showString("S")
    } else if (degrees < 315) {
        basic.showString("W")
    } else {
        basic.showString("N")
    }
})
