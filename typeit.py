import os, threading

cwd = os.getcwd()

def checkSpelling(file1, file2):
    f1 = open(cwd + rf'\typingTest\{file1}.txt', 'r')
    f2 = open(cwd + rf'\typingTest\{file2}.txt', 'r')

    i = 0
    j = 0
    k = 0
    
    for line1 in f1:
        i += 1

        for line2 in f2:

            # Matching line 1 from both files
            if line1 == line2:
                # Printing IDENTICAL if content is the same
                print("Line ", i, ": IDENTICAL")    
                j += 1
            else:
                # Printing the lines from both files
                print("Line ", i, ":")
                print("\tFile 1:", line1, end='')
                print("\tFile 2:", line2, end='')
                k += 1
            break

    print('Lines without mistakes: ', j)
    print('Lines with mistakes: ', k)
        
    f1.close()                                       
    f2.close()

print('This program checks correct spelling of your text file.\nIt must be .txt file.\nAfter the test time runs out close and save your text file.')

# Closing the file after the alloted time finishes (it is assumed the file in focus is the file you're typing into, that you want to test)
def fun():
    import pyautogui
    pyautogui.hotkey('ctrl', 's')
    pyautogui.hotkey('alt', 'f4')
    a = input('Type the name of the original file: ')
    b = input('Type the name of your test file: ')
    checkSpelling(a, b)

# Threading timer works in seconds, converting to minutes
delay_seconds = int(input('Enter the test time (in minutes): '))
#delay = delay_seconds*60
delay = delay_seconds

start_time = threading.Timer(delay, fun)
start_time.start()