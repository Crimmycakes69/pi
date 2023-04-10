import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the pin numbers for the PWM signals
pwm_pin1 = 18
pwm_pin2 = 19

# Set the frequency for the PWM signals
frequency = 1000

# Set up the PWM signals
GPIO.setup(pwm_pin1, GPIO.OUT)
GPIO.setup(pwm_pin2, GPIO.OUT)
pwm1 = GPIO.PWM(pwm_pin1, frequency)
pwm2 = GPIO.PWM(pwm_pin2, frequency)

# Start the PWM signals with duty cycle 0%
pwm1.start(0)
pwm2.start(0)

# Loop to alternate between the two PWM signals
while True:
    # Set duty cycle to 100% for PWM signal 1 and 0% for PWM signal 2
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(0)
    time.sleep(1)  # Wait for 1 second

    # Set duty cycle to 0% for PWM signal 1 and 100% for PWM signal 2
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(100)
    time.sleep(1)  # Wait for 1 second

# Clean up the GPIO pins when finished
GPIO.cleanup()
