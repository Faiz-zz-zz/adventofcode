d = {}
y = {}

def decide(j):
    if(j.isdigit()): return int(j)
    elif j in y: return y[j]
    return find(j)

def find(i):
    # print i, d[i]
    t = d[i].split()
    if len(t) == 3:
        if t[1] == "AND":
            y[i] = decide(t[0]) & decide(t[2])
            return y[i]
        elif t[1] == "OR":
            y[i] = decide(t[0]) | decide(t[2])
            return y[i]
        elif t[1] == "LSHIFT":
            y[i] = decide(t[0]) << int(t[2])
            return y[i]
        elif t[1] == "RSHIFT":
            y[i] = decide(t[0]) >> int(t[2])
            return y[i]
    elif len(t) == 2:
        y[i] = ~decide(t[1])
        return y[i]
    elif len(t) == 1:
        y[i] = decide(t[0])
        return y[i]

for _ in range(339):
    x = raw_input().split(" -> ")
    d[x[1]] = x[0]
a = find("a")
print a
d["b"] = str(a)
y = {}
print find("a")