# AFN: (aa|b)*(a|bb)*

transitions = {
    "0": {"a": "1", "b": "3"}, # Initial state
    "1": {"a": "2"},
    "2": {"a": "1", "b": "3"},
    "3": {"a": "4", "b": "5"},
    "4": {"a": "4", "b": "5"}, # Final state
    "5": {"a": "4", "b": "5"}  # Final state
}

finals = {"4", "5"}

def accept(string):
    state = "0"
    for symbol in string:
        if symbol not in {"a", "b"}:
            return False
        if symbol not in transitions[state]:
            return False
        state = transitions[state][symbol]
    if state in finals:
        return True
    else:
        return False

print(accept("aabb")) # True
print(accept("ab")) # False
print(accept("ba")) # True
print(accept("aabcbb")) # False
print(accept("aab")) # False
