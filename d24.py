input = open('d24.in').read().strip().split('\n\n')

initial_values = {}
gates = []

for line in input[0].split('\n'):
    wire, value = line.split(': ')
    initial_values[wire] = int(value)

for line in input[1].split('\n'):
    parts = line.split(' ')
    gates.append([parts[0], parts[1], parts[2], parts[4]])

def simulate_gates(wires1, gates):
    wires = wires1.copy()
    remaining_gates = gates[:]

    while remaining_gates:
        for gate in remaining_gates[:]:
            in1, operation, in2, out = gate
            if in1 in wires and in2 in wires:
                if operation == 'AND':
                    wires[out] = wires[in1] & wires[in2]
                elif operation == 'OR':
                    wires[out] = wires[in1] | wires[in2]
                elif operation == 'XOR':
                    wires[out] = wires[in1] ^ wires[in2]
                remaining_gates.remove(gate)

    output_bits = []
    for wire in sorted(wires):
        if wire.startswith('z'):
            output_bits.append(str(wires[wire]))

    return int(''.join(reversed(output_bits)), 2)


def part1():
    print(simulate_gates(initial_values, gates))

def part2():
    pass

part1()
part2()



  
