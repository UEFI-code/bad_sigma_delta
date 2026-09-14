avail_bits = 8
last_high_bits = 0
last_equ_energy = 0.0

def sigma_delta_step(expected_energy = 0.233):
    global last_high_bits, last_equ_energy
    energy_delta = expected_energy - last_equ_energy
    energy_sigma_bits = int(avail_bits * energy_delta)
    this_high_bits = last_high_bits + energy_sigma_bits
    if this_high_bits < 0: this_high_bits = 0
    if this_high_bits > avail_bits: this_high_bits = avail_bits
    this_equ_energy = this_high_bits / avail_bits
    print(f"Last equ energy: {last_equ_energy:.3f}, Energy delta: {energy_delta:.3f}, Energy sigma bits: {energy_sigma_bits}, This high bits: {this_high_bits}, This equ energy: {this_equ_energy:.3f}")
    last_high_bits = this_high_bits
    last_equ_energy = (last_equ_energy + this_equ_energy) / 2

for _ in range(16):
    sigma_delta_step(0.233)