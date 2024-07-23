from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    vari = random.randint(0, 3)
    # 2. Print your variable to the console
    print(vari)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title='awesome or not', prompt="what do you find awesome.")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if vari == 0:
      simpledialog.askstring(title='awesome or not', prompt="gee, thats so awesome!!")
    if vari == 1:
        simpledialog.askstring(title='awesome or not', prompt="thats ok...")
    if vari == 2:
        simpledialog.askstring(title='awesome or not', prompt="thats boring")
    if vari == 3:
        simpledialog.askstring(title='awesome or not', prompt="people like you are why the alpaca industry is dying.")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
