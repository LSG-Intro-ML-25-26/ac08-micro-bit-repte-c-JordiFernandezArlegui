input.onButtonPressed(Button.A, function () {
    radio.sendString(String2)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(String2)
})
let String2 = ""
String2 = "String"
