import Problem1
def problem1(input1, input2):
    # Put problem1 code here
    
    alphabet = "0 1 2 3 4 5 6 7 8 9".split()
    d = Problem1.gen_dfa(input2, alphabet)
    print("True means the number is not strongly divisible:",
          d.run_with_input_list(input1))
    
    return

def problem2():
    # Put problem2 code here
    return

def problem3():
    # Put problem3 code here
    return



def handle_prob1():
    u_input1 = list(str(input("Enter a number A to determine if A is strongly\
    divisible by B: ")))
    u_input2 = int(input("Enter a number B to determine if A is strongly divisible by B: "))

    problem1(u_input1, u_input2)
    return 

def handle_prob2():
    return

def handle_prob3():
    return


def main():
    handle_prob1()
    handle_prob2()
    handle_prob3()


if __name__ == "__main__":
    main()
    
