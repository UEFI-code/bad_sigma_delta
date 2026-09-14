avail_bits = 8
last_high_bits = 0
last_equ_energy = 0.0

def sigma_delta_step(expected_energy = 0.233, debug=False):
    global last_high_bits, last_equ_energy
    energy_delta = expected_energy - last_equ_energy
    energy_sigma_bits = int(avail_bits * energy_delta)
    this_high_bits = last_high_bits + energy_sigma_bits
    if this_high_bits < 0: this_high_bits = 0
    if this_high_bits > avail_bits: this_high_bits = avail_bits
    this_equ_energy = this_high_bits / avail_bits
    if debug:
        print(f"Last equ energy: {last_equ_energy:.3f}, Energy delta: {energy_delta:.3f}, Energy sigma bits: {energy_sigma_bits}, This high bits: {this_high_bits}, This equ energy: {this_equ_energy:.3f}")
    last_high_bits = this_high_bits
    last_equ_energy = (last_equ_energy + this_equ_energy) / 2

def get_byte_value():
    value = 0
    for _ in range(last_high_bits):
        value <<= 1
        value |= 1
    return value

if __name__ == "__main__":
    for _ in range(32):
        sigma_delta_step(0.233, debug=True)
        print(f"Byte value: {get_byte_value():08b}")