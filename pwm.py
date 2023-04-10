import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  # Pin 12 for PWM1
GPIO.setup(13, GPIO.OUT)  # Pin 32 for PWM2

# Set up PWM frequency and duty cycle
freq = 1000  # 1kHz frequency
dc = 50  # Duty Cycle

# Create PWM instances
pwm1 = GPIO.PWM(12, freq)
pwm2 = GPIO.PWM(13, freq)

# Start PWM signals
pwm1.start(dc)
pwm2.start(dc2)

# Set up phase shift
shift = 0.25  # 90 degrees shift
dc2 = (dc) * phase_shift
