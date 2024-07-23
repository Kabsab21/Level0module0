from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    ans1 = simpledialog.askstring(title='QUESTION 1', prompt="How likely is this code to run completly smooth with no errors?")
    if ans1 == "100%":
        score = score+1

    ans2 = simpledialog.askstring(title='QUESTION 2', prompt="How many times did i have to retype words in this sentence?")
    if ans2 == "6":
         score = score+1
    ans3 = simpledialog.askstring(title='QUESTION 3', prompt="free point, the answer is 4")
    if ans3 == "4":
         score = score+1
    #      // 3.  Use an if statement to check if their answer is correct
    finalscore = str(score)
    #      // 4.  if the user's answer was correct, add one to their score 
    simpledialog.askstring(title='FINALE', prompt="your final score is "+finalscore+" congrats i guess")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer

    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
