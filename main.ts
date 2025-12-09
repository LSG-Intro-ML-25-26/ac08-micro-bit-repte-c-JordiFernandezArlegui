radio.onReceivedNumber(function (receivedNumber) {
    if (num > 3) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendString(String2)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(String2)
})
input.onButtonPressed(Button.B, function () {
    num += randint(1, 6)
    radio.sendNumber(num)
})
let num = 0
let String2 = ""
String2 = "String"
