regs, prog = open('d17.in', 'r').read().split('\n\n')
regs = regs.split('\n')
A = int(regs[0].split(': ')[1])
B = int(regs[1].split(': ')[1])
C = int(regs[2].split(': ')[1])
prog = prog.split(': ')[1]
prog = list(map(int, prog.split(',')))

def run_program(A_init, B_init, C_init, program):
    A = A_init
    B = B_init
    C = C_init

    ip = 0

    outputs = []

    def combo_value(x):
        if x <= 3:
            return x
        elif x == 4:
            return A
        elif x == 5:
            return B
        elif x == 6:
            return C

    while ip < len(program):
        opcode = program[ip]
        if ip + 1 >= len(program):
            break
        operand = program[ip + 1]

        if opcode == 0:
            print(f"ip={ip}: opcode=0, operand={operand} -> A = A // (2 ** combo_value({operand}))")
        elif opcode == 1:
            print(f"ip={ip}: opcode=1, operand={operand} -> B = B ^ {operand}")
        elif opcode == 2:
            print(f"ip={ip}: opcode=2, operand={operand} -> B = combo_value({operand}) % 8")
        elif opcode == 3:
            print(f"ip={ip}: opcode=3, operand={operand} -> if A != 0: jump to {operand} else next")
        elif opcode == 4:
            print(f"ip={ip}: opcode=4, operand={operand} -> B = B ^ C")
        elif opcode == 5:
            print(f"ip={ip}: opcode=5, operand={operand} -> output combo_value({operand}) % 8")
        elif opcode == 6:
            print(f"ip={ip}: opcode=6, operand={operand} -> B = A // (2 ** combo_value({operand}))")
        elif opcode == 7:
            print(f"ip={ip}: opcode=7, operand={operand} -> C = A // (2 ** combo_value({operand}))")
        else:
            print(f"ip={ip}: opcode={opcode}, operand={operand} -> unknown opcode, stopping")

        if opcode == 0:  
            denom = 2 ** combo_value(operand)
            A = A // denom
            ip += 2

        elif opcode == 1:  
            B = B ^ operand
            ip += 2

        elif opcode == 2:  
            B = combo_value(operand) % 8
            ip += 2

        elif opcode == 3:  
            if A != 0:
                ip = operand
            else:
                ip += 2

        elif opcode == 4:  
            B = B ^ C
            ip += 2

        elif opcode == 5:  
            val = combo_value(operand) % 8
            outputs.append(str(val))
            ip += 2

        elif opcode == 6:  
            denom = 2 ** combo_value(operand)
            B = A // denom
            ip += 2

        elif opcode == 7:  
            denom = 2 ** combo_value(operand)
            C = A // denom
            ip += 2

        else:
            break

    return ",".join(outputs)


def r():
    A = 25986278
    B = 0
    C = 0

    outputs = []
    
    while A != 0:
        B = A % 8
        B = B ^ 4
        C = A // (2 ** B)
        B = B ^ C
        B = B ^ 4
        A = A // 8
        outputs.append(str(B % 8))
    
    return ",".join(outputs)

def part1():
    print(run_program(A, B, C, prog))
    print(r())

def find_initial_A(outputs):
    def backtrack(i, A_next):
        if i < 0:
            return A_next  
        
        for B0 in range(0,8):
            # A_i = (A_next * 8) + B0
            A_i = (A_next * 8) + B0
                
            if i == len(outputs)-1 and A_i == 0:
                continue
            
            # B1 = B0 ^ 4
            B1 = B0 ^ 4
            
            # C = A_i // (2^B1)
            C = A_i >> B1
            
            # B2 = B1 ^ C
            B2 = B1 ^ C
            
            # final_B = B2 ^ 4
            final_B = B2 ^ 4
            
            if (final_B % 8) == outputs[i]:
                res = backtrack(i-1, A_i)
                if res is not None:
                    return res
        return None
    
    return backtrack(len(outputs)-1, 0)

def part2():
    print(find_initial_A(prog))

part1()   
part2()
