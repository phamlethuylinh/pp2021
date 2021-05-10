import os

if __name__ == '__main__':
    exit = True
    os.system('Enter "exit" to get out')
    while exit:
        cmd = input(">>>>>>> ")
        if cmd == "exit":
            exit = False
        else:
            os.system(cmd)