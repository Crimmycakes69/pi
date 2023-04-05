import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)  # Pin 12 for PWM1
GPIO.setup(13, GPIO.OUT)  # Pin 32 for PWM2

# Set up PWM frequency and duty cycle
freq = 1000  # 1kHz frequency
duty_cycle_min = 50  # 50% duty cycle
duty_cycle_max = 100  # 100% duty cycle

# Create PWM instances
pwm1 = GPIO.PWM(12, freq)
pwm2 = GPIO.PWM(13, freq)

# Start PWM signals
pwm1.start(duty_cycle_min)
pwm2.start(duty_cycle_min)

# Set up phase shift
phase_shift = 0.25  # 90 degrees in terms of duty cycle
duty_cycle2 = (duty_cycle_min + duty_cycle_max) * phase_shift

# Generate PWM signals with phase shift
try:
    while True:
        # PWM1 at 50-100% duty cycle
        for dc in range(duty_cycle_min, duty_cycle_max + 1):
            pwm1.ChangeDutyCycle(dc)
            time.sleep(0.001)
        
        # PWM2 at 50-100% duty cycle with phase shift
        for dc in range(int(duty_cycle2), duty_cycle_max + 1):
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.001)
        for dc in range(duty_cycle_min, int(duty_cycle2)):
            pwm2.ChangeDutyCycle(dc)
            time.sleep(0.001)
            
except KeyboardInterrupt:
    # Clean up GPIO pins
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
