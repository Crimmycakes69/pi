import time
import rgpio

G1=12
G2=13

FREQ=1000
DUTY=50

ON_MICS = int(1e6 / FREQ * DUTY / 100.0)

sbc = rgpio.sbc()
if not sbc.connected:
   exit()

h = sbc.gpiochip_open(0) # Pi's main gpiochip

sbc.gpio_claim_output(h, G1) # claim G1 of gpiochip
sbc.gpio_claim_output(h, G2) # claim G2 of gpiochip

sbc.tx_pwm(h, G1, FREQ, DUTY)
sbc.tx_pwm(h, G2, FREQ, DUTY, pulse_offset=ON_MICS)

time.sleep(30)
