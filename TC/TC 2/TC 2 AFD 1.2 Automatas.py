# AFD: (aa|b)*(a|bb)*

transitions = {
    0: {"a": {0, 1}, "b": {0, 3}},
    1: {"a": {2}},
    2: {"a": {1}, "b": {3}},
    3: {"a": {4}, "b": {5}},
    4: {"a": {4}, "b": {5}},
    5: {"a": {4}, "b": {5}}
}

finals = {4, 5}

def accept(string):
    states = {0}
    for symbol in string:
        if symbol not in {"a", "b"}:
            return False
        new_states = set()
        for state in states:
            if symbol in transitions[state]:
                new_states.update(transitions[state][symbol])
        states = new_states
    if any(state in finals for state in states):
        return True
    else:
        return False

print(accept("aaabba")) # True
print(accept("ababbb")) # True
print(accept("aabbaa")) # False
print(accept("abbbba")) # False
print(accept("ac")) #False