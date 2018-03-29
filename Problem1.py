import numpy as np

class DFA:
    current_state = None

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = [start_state]
        return

    # Your gonna need to completely rewrite this
    def transition_to_state_with_input(self, input_value):
        new_current_state=[]
        for elem in self.current_state:
            # remove the first element of the current state
            if (elem, input_value) not in self.transition_function.keys():
                elem = None
                return

            val = self.transition_function[(elem, input_value)]
            for sElem in val:
                new_current_state.append(sElem)
        self.current_state = new_current_state[:]
        return


    def in_accept_state(self):
        for elem in self.current_state:
            if elem in self.accept_states:
                return False
        return True

    def go_to_initial_state(self):
        self.current_state = [self.start_state]
        return

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()

    def breadth_first_search(self, vertex):
        reach = np.zeros(len(self.states))
        parent = len(self.states) * [None]
        q = [vertex]
        while(len(q)>0):
            x = q.pop(0)
            for elem in self.alphabet:
                index = self.transition_function[x,elem]
                if reach[index] == 0:
                    reach[index] = 1
                    parent[index] = [x, elem]
                    q.append(index)
                    if index in self.accept_states:
                        return reach,parent
        return reach,parent

    def find_int(self, parents, reach):
        path = []
        if reach[0] == 0:
            return None
        current = 0
        while parents[current][0] != 0:
            if reach[current] != 0:
                path.append(parents[current][1])
                current = parents[current][0]
            else:
               break
        path.append(parents[current][1])
        path.reverse()
        return(path)


def gen_dfa(k, alphabet):
    states = set()
    for i in range(k):
        states.add(i)

    for i in range(len(alphabet)):
        alphabet[i] = int(alphabet[i])

    tf = dict()
    for current_state in states:
        for letter in alphabet:
            tf[str(current_state), str(letter)] = [str((10*current_state+letter) % k),
str(current_state)+"'"]

    for current_state in states:
        for letter in alphabet:
            tf[str(current_state)+"'", str(letter)] = [str((10*current_state+letter) % k)+"'"]

    accept_states = {'0',"0'"}
    start_state = "0"
    d = DFA(states, alphabet, tf, start_state, accept_states)


    return d


if __name__ == "__main__":
    u_input1 = list(str(input("Enter a number A to determine if A is strongly divisible by B: ")))
    u_input = int(input("Enter a number B to determine if A is strongly divisible by B: "))
    alphabet = "0 1 2 3 4 5 6 7 8 9".split()
    d = gen_dfa(u_input, alphabet)
    print("True means the number is not strongly divisible:", d.run_with_input_list(u_input1))

