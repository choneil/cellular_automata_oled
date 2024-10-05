h = 64
w = 128

row=[]*h
col=[]*w
cells = [[]]*w
nextCells=[]*w
ruleValue = 90
ruleSet = None
cells[0] = 0
cells[int(w/2-1)]=1

# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example for details
def rule_set(rule):
    binary = bin(ruleValue)
    print(binary)
    return binary
def calculate_state(a,b,c):
    neighborhood = " " + a + b + c
    value = 7 - int(neighborhood,2)
    return value
rule_set(ruleValue)