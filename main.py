import Problem1


def problem1(input1, input2):
    # Put problem1 code here
    
    alphabet = "0 1 2 3 4 5 6 7 8 9".split()
    d = Problem1.gen_dfa(input2, alphabet)
    print("True means the number is not strongly divisible:",
          d.run_with_input_list(input1))
    
    return

def problem2(filename, egrep_string):
    # Put problem2 code here
    # teestoost thiis fiile
    import subprocess
    cmd = 'egrep'

    # String used to complete problem 2
    cmd_list = [cmd, egrep_string, filename]
    subprocess.run(cmd_list)
    return

def prob3_readfile(filename):
    f = open(filename, 'r')
    n,k = f.readline().split()
    F = f.readline().split()
    F = [int(y) for y in F]
    delta = [line.split() for line in f]
    delta = [[int(y) for y in x] for x in delta]
    sigma = []
    for i in range(0, int(k)):
        sigma.append(i)
        
    DFA = {}
    DFA['Sigma'] = sigma
    DFA['delta'] = delta
    DFA['F'] = F
    f.close()
    return DFA

def problem3():
    file_1 = "dfa1.txt"
    file_2 = "dfa2.txt"
    output_file = "dfa3.txt"

    DFA_1 = prob3_readfile(file_1)
    DFA_2 = prob3_readfile(file_2)

    # combine the 2 dfas into one.
    delta_one = DFA_1['delta']
    delta_two = DFA_2['delta']

    Q = []
    start_state = [0,0]
    Q.append(start_state)
    delta_prime = []
    for i in range(0, len(DFA_1['Sigma'])):
        delta_prime.append([])
        
    for state in Q:
        for L in DFA_1['Sigma']:
            cs = [delta_one[state[0]][L], delta_two[state[1]][L]]
            if not cs in Q:
                Q.append(cs)
            delta_prime[L].append(cs)

            
    F = []  
    for i in range(0, len(Q)):
        if Q[i][0] in DFA_1['F'] and Q[i][1] in DFA_2['F']:
            F.append(i)

    # remap delta_prime from a table of tuples to our new
    # combined transition table
    for i in range(0, len(delta_prime)):
        for j in range(0, len(delta_prime[0])):
            for k in range(0, len(Q)):
                if delta_prime[i][j] == Q[k]:
                    delta_prime[i][j] = k

    sigma = [] 
    for i in range(0, len(delta_prime)):
        sigma.append(i)
        
    output_to_file(output_file, Q, sigma, delta_prime, F)
    return

def output_to_file(filename, Q, sigma, delta, F):
    f = open(filename, 'w+')
    f.write(str(len(Q)) + " " + str(len(sigma)) + "\n")
    t = ""
    for x in F:
        t += str(x) + " "
    f.write(t + "\n") 
    for i in range(0, len(delta[0])):
        t = ""
        for j in range(0, len(delta)):
            t += str(delta[j][i]) + " "
        f.write(t + "\n")

    f.close()
    return

def handle_prob1():
    u_input1 = list(str(input("Enter a number A to determine if A is strongly divisible by B: ")))
    u_input2 = int(input("Enter a number B to determine if A is strongly divisible by B: "))

    problem1(u_input1, u_input2)
    return 

def handle_prob2():
    egrep_string = '.*(.)\\1.*(.)\\2.*'
    filename = input("Relative path to file to egrep using " + egrep_string + " ")
    problem2(filename, egrep_string)
    return

def handle_prob3():
    problem3()
    print("dfa1.txt intersection dfa2.txt saved as dfa3.txt")
    return


def main():
    while(True):
        user_input = input("\nProblem 1, 2, 3 or quit. (1,2,3,q) ")
        user_input = user_input.strip()
        if user_input == '1':
            handle_prob1()
        elif user_input == '2':
            handle_prob2()
        elif user_input == '3':
            handle_prob3()
        elif user_input == 'q':
            break
        else:
            continue


if __name__ == "__main__":
    main()
    
