from collections import deque

# Rainbow colors represented by colored circles
R = "🔴"   # Red
O = "🟠"   # Orange
Y = "🟡"   # Yellow
G = "🟢"   # Green
B = "🔵"   # Blue
I = "🟣"   # Indigo
V = "🟤"   # Violet (using brown as a placeholder)
_ = "⬜"   # Blank tile

# Initial State
start = (
    (R, O, Y),
    (G, _, B),
    (I, V, "⚫")
)

# Goal State
goal = (
    (R, O, Y),
    (G, B, "⚫"),
    (I, V, _)
)

# Print puzzle
def print_state(state):
    for row in state:
        print(" ".join(row))
    print()

print("Initial State:")
print_state(start)

print("Goal State:")
print_state(goal)
