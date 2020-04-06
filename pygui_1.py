import tkinter as tk
#creating window
window = tk.Tk()

#labels are for displaying text and images, text can't be edited by user
greeting = label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white, fg can be written instead of foreground, bg for background
    background="black",  # Set the background color to black
    width=15,
    height=10 
)
#pack to put the label on window
#greeting.pack()

#color charts for tkinter http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
# also hex color code work here. tools for getting hex code https://htmlcolorcodes.com


#button
button = tk.Button(
    text="Hello Mr. Shahir",
    fg="white",
    bg="black",
    width="15",
    height="5"
)
#button.pack()


#getting user input with Entry Widgets
'''
 There are three main operations that you can perform with Entry widgets:
Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()
'''
label_for_entry = tk.Label(text="Name")
entry = tk.Entry(fg="black", bg="white", width=50)
label_for_entry.pack()
entry.pack()
#entry get
name = entry.get()
#delete 
'''
Entry.delete() works just like string slicing. 
The first argument determines the starting index, 
and the deletion continues up to but not including the index passed as the second argument. 
Use the special constant tk.END for the second argument of .delete() to remove all text in an Entry
'''
entry.delete(0,4) #deletes the first 4 characters, tk.END is end of string
#insert text to the entry
'''
The first argument tells .insert() where to insert the text. 
If there is no text in the Entry, then the new text will always be inserted at the beginning of the widget, no matter what value you pass as the first argument.
 For example, calling .insert() with 100 as the first argument instead of 0, as you did above, would have generated the same output.
If an Entry already contains some text, then .insert() will insert the new text at the specified position and shift all existing text to the right:
'''
entry.insert(0, "Mr.")

#getting multiple user input with Text Widgets
'''
Text widgets are used for entering text, just like Entry widgets. 
The difference is that Text widgets may contain multiple lines of text.
With a Text widget, a user can input a whole paragraph or even several pages of text!
Just like Entry widgets, there are three main operations you can perform with Text widgets:
Retrieve text with .get()
Delete text with .delete()
Insert text with .insert()
Although the method names are the same as the Entry methods, they work a bit differently.
'''
text_box = tk.Text()
text_box.pack()
#get text
'''
Just like Entry widgets, you can retrieve the text from a Text widget using .get().
However, calling .get() with no arguments doesn’t return the full text in the text box like it does for Entry widgets. 
It raises an exception. so u need to pass start and end index
Text.get() required at least one argument. 
Calling .get() with a single index returns a single character. 
To retrieve several characters, you need to pass a start index and an end index. 
Indices in Text widgets work differently than Entry widgets. 
Since Text widgets can have several lines of text, an index must contain two pieces of information:
1. The line number of a character
2. The position of a character on that line
Line numbers start with 1, and character positions start with 0.
To make an index, you create a string of the form "<line>.<char>", replacing <line> with the line number and <char> with the character number.
For example, "1.0" represents the first character on the first line, and "2.3" represents the fourth character on the second line.
'''
# get first line if the text is hello
hello = text_box.get("1.0", "1.5")
#get all the text from text box
text = text_box.get("1.0", tk.END) #will return hello\nworld\n
#delete
'''
.delete() is used to delete characters from a text box. It work just like .delete() for Entry widgets. There are two ways to use .delete():
With a single argument
With two arguments
Using the single-argument version, you pass to .delete() the index of a single character to be deleted. For example, the following deletes the first character H from the text box:
With the two-argument version, you pass two indices to delete a range of characters starting at the first index and up to, but not including, the second index.
For example, to delete the remaining "ello" on the first line of the text box, use the indices "1.0" and "1.4":
Even though you can’t see it, there’s still a character on the first line. It’s a newline character! You can verify this using .get():
If you delete that character, then the rest of the contents of the text box will shift up a line:
'''
#insert into text box
'''
text_box.insert("1.0", "Hello")
If you want to insert text onto a new line, then you need to insert a newline character manually into the string being inserted:
text_box.insert("2.0", "\nWorld")
.insert() will do one of two things:

Insert text at the specified position if there’s already text at or after that position.
Append text to the specified line if the character number is greater than the index of the last character in the text box.
It’s usually impractical to try and keep track of what the index of the last character is. The best way to insert text at the end of a Text widget is to pass tk.END to the first parameter of .insert():

text_box.insert(tk.END, "Put me at the end!")
Don’t forget to include the newline character (\n) at the beginning of the text if you want to put it on a new line:

text_box.insert(tk.END, "\nPut me on a new line!")
'''

'''
Label, Button, Entry, and Text widgets are just a few of the widgets available in Tkinter. There are several others, including widgets for checkboxes, radio buttons, scroll bars, and progress bars. For more information on all of the available widgets, see the Additional Widgets list in the Additional Resources section.
'''
#without mainloop, nothing will be shown
window.mainloop()
#window.destroy()