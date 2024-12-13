import z3

def solve_machine(ax,ay,bx,by,tx,ty, offset):
    tx += offset
    ty += offset

    A = z3.Int('A')
    B = z3.Int('B')
    s = z3.Solver()
    s.add(ax*A + bx*B == tx)
    s.add(ay*A + by*B == ty)
    if s.check() == z3.sat:
        m = s.model()
        return 3*m[A].as_long() + m[B].as_long()
    return 0

def parse_machines(lines):
    def parse_line(line, prefix):
        part = line[len(prefix):].strip()
        xpart, ypart = [p.strip() for p in part.split(',')]

        x_val = int(xpart[2:])
        y_val = int(ypart[2:])

        return x_val, y_val
    
    machines = []
    for i in range(0,len(lines),3):
        aX,aY = parse_line(lines[i], "Button A:")
        bX,bY = parse_line(lines[i+1], "Button B:")
        tX,tY = parse_line(lines[i+2], "Prize:")
        machines.append((aX,aY,bX,bY,tX,tY))
    return machines

def part1():
    machines = parse_machines([line.strip() for line in open("d13.in","r").readlines() if line.strip()])
    res = 0
    for (aX,aY,bX,bY,tX,tY) in machines:
        res += solve_machine(aX,aY,bX,bY,tX,tY, 0)
    print(res)

def part2():
    machines = parse_machines([line.strip() for line in open("d13.in","r").readlines() if line.strip()])
    res = 0
    for (aX,aY,bX,bY,tX,tY) in machines:
        res += solve_machine(aX,aY,bX,bY,tX,tY, 10000000000000)
    print(res)

part1()
part2()
