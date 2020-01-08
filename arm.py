import RPi.GPIO as GPIO
import time

baseServoPIN = 17
leftServoPIN = 23
rightServoPIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(baseServoPIN, GPIO.OUT)
GPIO.setup(leftServoPIN, GPIO.OUT)
GPIO.setup(rightServoPIN, GPIO.OUT)

baseServo = GPIO.PWM(baseServoPIN, 50)  # GPIO 17 for PWM with 50Hz
leftServo = GPIO.PWM(leftServoPIN, 50)  # GPIO 23
rightServo = GPIO.PWM(rightServoPIN, 50)  # GPIO 22

baseServo.start(0)  # Initialization
leftServo.start(0)
rightServo.start(0)

delay = .08

baseServoRightBound = 3
baseServoLeftBound = 11
leftServoBottomBound = 6
leftServoTopBound = 11
rightServoBottomBound = 7
rightServoTopBound = 2


def projectDemo():
    moveBaseServo()
    time.sleep(delay * 2)
    baseServo.ChangeDutyCycle(7)
    time.sleep(delay)
    leftServo.ChangeDutyCycle(7)
    time.sleep(delay)
    moveRightServo()
    time.sleep(delay * 2)
    moveLeftServo()
    time.sleep(delay * 2)

    pickUpDemo()


def pickUpDemo():
    delay = .3
    rightServo.ChangeDutyCycle(3)
    time.sleep(delay)
    baseServo.ChangeDutyCycle(9)
    time.sleep(1)
    moveArmDownThenUp()
    time.sleep(1)
    baseServo.ChangeDutyCycle(5)
    time.sleep(delay)
    moveArmDownThenUp()
    time.sleep(1)
    baseServo.ChangeDutyCycle(7)


def moveArmDownThenUp():
    leftServo.ChangeDutyCycle(10)
    time.sleep(delay)
    rightServo.ChangeDutyCycle(3)
    time.sleep(delay)

    for y in range(3, 7):
        rightServo.ChangeDutyCycle(y)
        time.sleep(delay)
    for x in range(10, 6, -1):
        leftServo.ChangeDutyCycle(x)
        time.sleep(delay)
    for x in range(6, 10):
        leftServo.ChangeDutyCycle(x)
        time.sleep(delay)
    for y in range(7, 3, -1):
        rightServo.ChangeDutyCycle(y)
        time.sleep(delay)


def moveBaseServo():
    baseServo.ChangeDutyCycle(baseServoRightBound)
    time.sleep(delay)
    step = baseServoRightBound
    while step <= baseServoLeftBound:
        baseServo.ChangeDutyCycle(step)
        step += .5
        time.sleep(delay)
    while step >= baseServoRightBound:
        baseServo.ChangeDutyCycle(step)
        step -= .5
        time.sleep(delay)


def moveLeftServo():
    leftServo.ChangeDutyCycle(leftServoTopBound)
    rightServo.ChangeDutyCycle(4)
    step = leftServoTopBound
    while step >= leftServoBottomBound:
        leftServo.ChangeDutyCycle(step)
        step -= .5
        time.sleep(delay)
    while step <= leftServoTopBound:
        leftServo.ChangeDutyCycle(step)
        step += .5
        time.sleep(delay)


def moveRightServo():
    rightServo.ChangeDutyCycle(rightServoTopBound)
    step = rightServoTopBound
    while step <= rightServoBottomBound:
        rightServo.ChangeDutyCycle(step)
        step += .5
        time.sleep(delay)
    while step >= rightServoTopBound:
        rightServo.ChangeDutyCycle(step)
        step -= .5
        time.sleep(delay)


projectDemo()
