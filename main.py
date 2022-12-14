# Import modules
import os, sys, tty, termcolor

def find_plugin_name () :
    print ("Finding plugin name")

from highlighting_placeholder import dunno_name

# I can read the placeholder and at the start write code from plugin file to placeholder file

index = 0
input = ""



def command_line():
    tty.setraw(sys.stdin)
    while True: # loop for each line
    # Define data-model for an input-string with a cursor
        input = ""
        index = 0
        while True: # loop for each character
            char = ord(sys.stdin.read(1)) # read one char and get char code

            # ELif char == CTR-C
            if char == 3:
                return

            elif 32 <= char <= 126:
                #Store letter in index
                input = input[:index] + chr(char) + input[index:]
                index += 1

            elif char in {10, 13}:
                sys.stdout.write(u"\u001b[1000D")
                print ()
                os.system(input)
                input = ""
                index = 0

            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 68: # Left
                        index = max(0, index - 1)
                    elif next2 == 67: # Right
                        index = min(len(input), index + 1)

            #Elif char == backspace
            elif char == 127 :
                input = input[:index-1] + input[index:]
                index -= 1

            # Print current input-string
            sys.stdout.write(u"\u001b[1000D") # Move all the way left
            sys.stdout.write(u"\u001b[0K")    # Clear the line
            sys.stdout.write(dunno_name(input))
            sys.stdout.write(u"\u001b[1000D") # Move all the way left again

            if index > 0:
                sys.stdout.write(u"\u001b[" + str(index) + "C") # Move cursor too index
            sys.stdout.flush()

command_line()