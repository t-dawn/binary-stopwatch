start = 0
elapsedtime = 0
digit = 0
"""

this loop was to test the accuracy of the column counting in our draw binary code

"""
def drawBinary(column: number, decimal: number):
    if decimal == 1:
        led.plot(column, 1)
    elif decimal == 2:
        led.plot(column, 2)
    elif decimal == 3:
        led.plot(column, 1)
        led.plot(column, 2)
    elif decimal == 4:
        led.plot(column, 3)
    elif decimal == 5:
        led.plot(column, 3)
        led.plot(column, 1)
    elif decimal == 6:
        led.plot(column, 3)
        led.plot(column, 2)
    elif decimal == 7:
        led.plot(column, 3)
        led.plot(column, 2)
        led.plot(column, 1)
    elif decimal == 8:
        led.plot(column, 4)
    elif decimal == 9:
        led.plot(column, 4)
        led.plot(column, 1)
    elif decimal == 0:
        led.plot(column, 0)
    else:
        pass
"""

the video describes how binary numbers and time works at 7:30.

"""

def on_button_pressed_a():
    global start
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global elapsedtime, digit
    basic.clear_screen()
    # this is about 34 minutes into the video tutorial. Following the for loop instruction.
    # 
    elapsedtime = Math.round((input.running_time() - start) / 1000)
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
basic.forever(on_forever)
