import time
import pwmio
import board

# Initialize PWM output on a single pin (simulate motor 1)
pwm_motor = pwmio.PWMOut(board.D9, frequency=50, duty_cycle=0)  # 50 Hz typical for servos/ESCs

print("Starting PWM motor simulation...")

# Gradually increase and decrease duty cycle
try:
    while True:
        # Simulate motor throttle increase
        for duty in range(0, 65535, 2000):  # From 0% to 100%
            pwm_motor.duty_cycle = duty
            print(f"Throttle: {duty / 65535 * 100:.1f}%")
            time.sleep(0.05)

        # Simulate motor throttle decrease
        for duty in range(65535, 0, -2000):  # From 100% to 0%
            pwm_motor.duty_cycle = duty
            print(f"Throttle: {duty / 65535 * 100:.1f}%")
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Simulation stopped.")
    pwm_motor.deinit()
