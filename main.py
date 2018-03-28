
def problem1():
    # Put problem1 code here
    return

def problem2(filename):
    # Put problem2 code here
    # teestoost thiis fiile
    import subprocess
    cmd = 'egrep'

    # String used to complete problem 2
    egrep_string = '.*(.)\\1.*(.)\\2.*'

    
    cmd_list = [cmd, egrep_string, filename]
    subprocess.run(cmd_list)
    return

def problem3():
    # Put problem3 code here
    return



def handle_prob1():
    problem1()
    return 

def handle_prob2():
    filename = input("File to egrep(note - whitespace is considered in the language): ")
    problem2(filename)
    return

def handle_prob3():
    problem3()
    return


def main():
    handle_prob1()
    handle_prob2()
    handle_prob3()


if __name__ == "__main__":
    main()
    
