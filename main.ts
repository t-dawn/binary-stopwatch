let start = 0
let elapsedtime = 0
let digit = 0
/**
 * this loop was to test the accuracy of the column counting in our draw binary code
 */
function drawBinary (column: number, decimal: number) {
    if (decimal == 1) {
        led.plot(column, 1)
    } else if (decimal == 2) {
        led.plot(column, 2)
    } else if (decimal == 3) {
        led.plot(column, 1)
        led.plot(column, 2)
    } else if (decimal == 4) {
        led.plot(column, 3)
    } else if (decimal == 5) {
        led.plot(column, 3)
        led.plot(column, 1)
    } else if (decimal == 6) {
        led.plot(column, 3)
        led.plot(column, 2)
    } else if (decimal == 7) {
        led.plot(column, 3)
        led.plot(column, 2)
        led.plot(column, 1)
    } else if (decimal == 8) {
        led.plot(column, 4)
    } else if (decimal == 9) {
        led.plot(column, 4)
        led.plot(column, 1)
    } else if (decimal == 0) {
        led.plot(column, 0)
    } else {
    	
    }
}
/**
 * the video describes how binary numbers and time works at 7:30.
 */
input.onButtonPressed(Button.A, function () {
    start = input.runningTime()
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
basic.forever(function () {
    basic.clearScreen()
    // this is about 34 minutes into the video tutorial. Following the for loop instruction.
    // 
    elapsedtime = Math.round((input.runningTime() - start) / 1000)
    digit = Math.idiv(elapsedtime, 100000)
    drawBinary(0, digit)
    elapsedtime = elapsedtime % 10000
    digit = Math.idiv(elapsedtime, 1000)
    drawBinary(1, digit)
    elapsedtime = elapsedtime % 1000
    digit = Math.idiv(elapsedtime, 100)
    drawBinary(2, digit)
    elapsedtime = elapsedtime % 100
    digit = Math.idiv(elapsedtime, 10)
    drawBinary(3, digit)
    elapsedtime = elapsedtime % 10
    elapsedtime = elapsedtime % 1
    drawBinary(4, digit)
})
