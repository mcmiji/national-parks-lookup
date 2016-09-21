
"""
National Parks Lookup Tool
There is a global dictionary that contains National Parks by name.
GUI for the user to easily input the state.
The core logic is in the main() function.
"""


from Tkinter import *
'''
This is a simple GUI example.
There is a label, text entry box, and button.
When the button is clicked, a function is executed.
'''
root_widget = Tk()

var_parks_text = StringVar()
entry_text = Entry()                        # creates a text entry box

# def set_text():
#     var_label_text.set(entry_text.get())

#import module from the py file within same folder
from national_parks_by_state import national_parks_by_state


def check_for_state(state):
    state = state.lower()
    if state in national_parks_by_state:
        return True
    else: 
        return False

def onOk():
    state = entry_text.get()
    if check_for_state(state):
        parks = national_parks_by_state[state]
        parks_str = "\n".join(parks)
        var_parks_text.set(str(parks_str))     #string variable, used as the label(below)
    else:
        var_parks_text.set("This state is lame!")




def main():

                            # creates a widget window which will hold all other widgets.
    root_widget.geometry("400x300")             # sets the size of the window
    root_widget.title("National Parks Lookup")        # set the title of the window

    var_label_text = StringVar()                # Special Tkinter Variable for label text

    var_label_text.set("Which state would you like to visit?") #text that goes in the white spot
    lbl_enter_state = Label(root_widget, textvariable=var_label_text) #white spot
    lbl_enter_state.pack()                            # show the label

    entry_text.insert(0, "Type the entire name.")   # text to display on start up
    entry_text.pack()                           # show the entry box
                     # show the label

    # create a button
    # command sets a function to run when the button is CLICKED. AKA as an event and callback
    # command expects the NAME of the function not to call it.
    btn_ok = Button(text='OK', command=onOk)
    #btn_ok = Button(text='Ok', command=set_text)
    btn_ok.pack()


    lbl_parks = Label(root_widget, textvariable=var_parks_text)
    lbl_parks.pack()       

    # runs the window in a loop so it continuously detects the button click event
    root_widget.mainloop()



if __name__ == '__main__':
    main()
