import tkinter as tk
'''
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
'''
#color charts for tkinter http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
# also hex color code work here. tools for getting hex code https://htmlcolorcodes.com

'''
#button
button = tk.Button(
    text="Hello Mr. Shahir",
    fg="white",
    bg="black",
    width="15",
    height="5"
)
#button.pack()
'''

#getting user input with Entry Widgets
'''
 There are three main operations that you can perform with Entry widgets:
Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()
'''
#label_for_entry = tk.Label(text="Name")
#entry = tk.Entry(fg="black", bg="white", width=50)
#label_for_entry.pack()
#entry.pack()
#entry get
#name = entry.get()
#delete 
'''
Entry.delete() works just like string slicing. 
The first argument determines the starting index, 
and the deletion continues up to but not including the index passed as the second argument. 
Use the special constant tk.END for the second argument of .delete() to remove all text in an Entry
'''
#entry.delete(0,4) #deletes the first 4 characters, tk.END is end of string
#insert text to the entry
'''
The first argument tells .insert() where to insert the text. 
If there is no text in the Entry, then the new text will always be inserted at the beginning of the widget, no matter what value you pass as the first argument.
 For example, calling .insert() with 100 as the first argument instead of 0, as you did above, would have generated the same output.
If an Entry already contains some text, then .insert() will insert the new text at the specified position and shift all existing text to the right:
'''
#entry.insert(0, "Mr.")

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
#text_box = tk.Text()
#text_box.pack()
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
#hello = text_box.get("1.0", "1.5")
#get all the text from text box
#text = text_box.get("1.0", tk.END) #will return hello\nworld\n
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

#frame
'''
Frame widgets are important for organizing the layout of your widgets in an application.
Frames are best thought of as containers for other widgets. 
You can assign a widget to a frame by setting the widget’s master attribute. 
Since label_b is assigned to frame_b, it moves to wherever frame_b is positioned.

All four of the widget types you’ve learned about—Label, Button, Entry, and Text—have a master attribute that’s set when you instantiate them. 
That way, you can control which Frame a widget is assigned to. 
Frame widgets are great for organizing other widgets in a logical manner. 
Related widgets can be assigned to the same frame so that, if the frame is ever moved in the window, then the related widgets stay together.
'''
#frame_a = tk.Frame()
#frame_b = tk.Frame()
#label_a = tk.Label(master=frame_a, text="I'm in Frame A")
#label_a.pack()
#label_b = tk.Label(master=frame_b, text="I'm in Frame B")
#label_b.pack()
#frame_a.pack()
#frame_b.pack()

#adjusting frame appearance with reliefs
'''
Frame widgets can be configured with a relief attribute that creates a border around the frame. You can set relief to be any of the following values:
tk.FLAT: Has no border effect (the default value).
tk.SUNKEN: Creates a sunken effect.
tk.RAISED: Creates a raised effect.
tk.GROOVE: Creates a grooved border effect.
tk.RIDGE: Creates a ridged effect.
To apply the border effect, you must set the borderwidth attribute to a value greater than 1. 
This attribute adjusts the width of the border in pixels. 
The best way to get a feel for what each effect looks like is to see them for yourself. 
Here’s a script that packs five Frame widgets into a window, each with a different value for the relief argument
'''
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
'''
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    #frame.pack(side=tk.LEFT) #packs the Frame into the window using .pack(). The side keyword argument tells Tkinter in which direction to pack the frame objects. You’ll see more about how this works in the next section.
    label = tk.Label(master=frame, text=relief_name)
    #label.pack()
'''
#controlling layouts using geometric manager
'''
Up until now, you’ve been adding widgets to windows and Frame widgets using .pack(), but you haven’t learned what exactly this method does. 
Let’s clear things up! Application layout in Tkinter is controlled with geometry managers. 
While .pack() is an example of a geometry manager, it isn’t the only one. 
Tkinter has two others:
.place()
.grid()
Each window and Frame in your application can use only one geometry manager. 
However, different frames can use different geometry managers, even if they’re assigned to a frame or window using another geometry manager. 
Start by taking a closer look at .pack().

.pack() uses a packing algorithm to place widgets in a Frame or window in a specified order. 
For a given widget, the packing algorithm has two primary steps:
Compute a rectangular area called a parcel that’s just tall (or wide) enough to hold the widget and fills the remaining width (or height) in the window with blank space.
Center the widget in the parcel unless a different location is specified.
.pack() is powerful, but it can be difficult to visualize. 
The best way to get a feel for .pack() is to look at some examples. 
See what happens when you .pack() three Label widgets into a Frame
'''
#frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
#frame1.pack()
#frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
#frame2.pack()
#frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
#frame3.pack()
'''
There are three invisible parcels containing each of the three Frame widgets. Each parcel is as wide as the window and as tall as the Frame that it contains. Since no anchor point was specified when .pack() was called for each Frame, they’re all centered inside of their parcels. That’s why each Frame is centered in the window.

.pack() accepts some keyword arguments for more precisely configuring widget placement. For example, you can set the fill keyword argument to specify in which direction the frames should fill. The options are tk.X to fill in the horizontal direction, tk.Y to fill vertically, and tk.BOTH to fill in both directions. Here’s how you would stack the three frames so that each one fills the whole window horizontally
'''
#frame1.pack(fill=tk.X)
#frame2.pack(fill=tk.X)
#frame3.pack(fill=tk.X)
#side keyword in .pack()
'''
The side keyword argument of .pack() specifies on which side of the window the widget should be placed. These are the available options:
tk.TOP
tk.BOTTOM
tk.LEFT
tk.RIGHT
If you don’t set side, then .pack() will automatically use tk.TOP and place new widgets at the top of the window, or at the top-most portion of the window that isn’t already occupied by a widget. For example, the following script places three frames side-by-side from left to right and expands each frame to fill the window vertically
'''
#frame1.pack(fill=tk.Y, side=tk.LEFT)
#frame2.pack(fill=tk.Y, side=tk.LEFT)
#frame3.pack(fill=tk.Y, side=tk.LEFT)
'''
To make the layout truly responsive, you can set an initial size for your frames using the width and height attributes. Then, set the fill keyword argument of .pack() to tk.BOTH and set the expand keyword argument to True
'''
#frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#The .place() geometry manager
'''
You can use .place() to control the precise location that a widget should occupy in a window or Frame. You must provide two keyword arguments, x and y, which specify the x- and y-coordinates for the top-left corner of the widget. Both x and y are measured in pixels, not text units.

Keep in mind that the origin (where x and y are both 0) is the top-left corner of the Frame or window. So, you can think of the y argument of .place() as the number of pixels from the top of the window, and the x argument as the number of pixels from the left of the window.
'''
#frame = tk.Frame(master=window, width = 150, height = 150)
#frame.pack()
#label1 = tk.Label(master=frame, text="i'm at (0,0)", bg="red")
#label1.place(x=0,y=0)

#label2 = tk.Label(master=frame, text="i'm at (65,56)", bg="yellow")
#label2.place(x=65,y=56)
'''
.place() is not used often. It has two main drawbacks:

Layout can be difficult to manage with .place(). This is especially true if your application has lots of widgets.
Layouts created with .place() are not responsive. They don’t change as the window is resized.
One of the main challenges of cross-platform GUI development is making layouts that look good no matter which platform they are viewed on, and .place() is a poor choice for making responsive and cross-platform layouts.
'''

#the .grid() geometry manager 
'''
The geometry manager you’ll likely use most often is .grid(), which provides all the power of .pack() in a format that’s easier to understand and maintain.

.grid() works by splitting a window or Frame into rows and columns. You specify the location of a widget by calling .grid() and passing the row and column indices to the row and column keyword arguments, respectively. Both row and column indices start at 0, so a row index of 1 and a column index of 2 tells .grid() to place a widget in the third column of the second row.
'''
#The following script creates a 3 × 3 grid of frames with Label widgets packed into them:
'''
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i,column=j) #Each Frame is attached to the window with the .grid() geometry manager
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack() #Each label is attached to its master Frame with .pack()
'''
'''
The important thing to realize here is that even though .grid() is called on each Frame object, the geometry manager applies to the window object. Similarly, the layout of each frame is controlled with the .pack() geometry manager.
'''

'''
The frames in the previous example are placed tightly next to one another. To add some space around each Frame, you can set the padding of each cell in the grid. Padding is just some blank space that surrounds a widget and separates it visually from its contents.

The two types of padding are external and internal padding. External padding adds some space around the outside of a grid cell. It’s controlled with two keyword arguments to .grid():

padx adds padding in the horizontal direction.
pady adds padding in the vertical direction.
Both padx and pady are measured in pixels, not text units, so setting both of them to the same value will create the same amount of padding in both directions. Try to add some padding around the outside of the frames in the previous example

.pack() also has padx and pady parameters. The following code is nearly identical to the previous code, except that you add 5 pixels of additional padding around each Label in both the x and y directions
'''
'''
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=tk.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack(padx=5,pady=5)
'''


#for making responsive window while resizing 
'''
You can adjust how the rows and columns of the grid grow as the window is resized using .columnconfigure() and .rowconfigure() on the window object. Remember, the grid is attached to window, even though you’re calling .grid() on each Frame widget. Both .columnconfigure() and .rowconfigure() take three essential arguments:

The index of the grid column or row that you want to configure (or a list of indices to configure multiple rows or columns at the same time)
A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows
A keyword argument called minsize that sets the minimum size of the row height or column width in pixels
weight is set to 0 by default, which means that the column or row doesn’t expand as the window resizes. If every column and row is given a weight of 1, then they all grow at the same rate. If one column has a weight of 1 and another a weight of 2, then the second column expands at twice the rate of the first. Adjust the previous script to better handle window resizing
'''
'''
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)
'''
'''
.columnconfigure() and .rowconfigure() are placed in the body of the outer for loop. (You could explicitly configure each column and row outside of the for loop, but that would require writing an additional six lines of code.)

On each iteration of the loop, the i-th column and row are configured to have a weight of 1. This ensures that each row and column expands at the same rate whenever the window is resized. The minsize argument is set to 75 for each column and 50 for each row. This makes sure the Label widget always displays its text without chopping off any characters, even if the window size is extremely small.

The result is a grid layout that expands and contracts smoothly as the window is resized
'''

'''
By default, widgets are centered in their grid cells. For example, the following code creates two Label widgets and places them in a grid with one column and two rows
'''
'''
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)
'''
'''
You can change the location of each label inside of the grid cell using the sticky parameter. sticky accepts a string containing one or more of the following letters:

"n" or "N" to align to the top-center part of the cell
"e" or "E" to align to the right-center side of the cell
"s" or "S" to align to the bottom-center part of the cell
"w" or "W" to align to the left-center side of the cell
The letters "n", "s", "e", and "w" come from the cardinal directions north, south, east, and west. Setting sticky to "n" on both Labels in the previous code positions each Label at the top-center of its grid cell
'''
'''
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")
'''
'''
You can combine multiple letters in a single string to position each Label in the corner of its grid cell
In this example, the sticky parameter of label1 is set to "ne", which places the label at the top-right corner of its grid cell. label2 is positioned in the bottom-left corner by passing "sw" to sticky
'''
'''
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")
'''

'''
When a widget is positioned with sticky, the size of the widget itself is just big enough to contain any text and other contents inside of it. It won’t fill the entire grid cell. In order to fill the grid, you can specify "ns" to force the widget to fill the cell in the vertical direction, or "ew" to fill the cell in the horizontal direction. To fill the entire cell, set sticky to "nsew". The following example illustrates each of these options
'''
'''
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")
'''

'''
What the above example illustrates is that the .grid() geometry manager’s sticky parameter can be used to achieve the same effects as the .pack() geometry manager’s fill parameter. The correspondence between the sticky and fill parameters is summarized in the following table:

    .grid()	        .pack()

    sticky="ns"	    fill=tk.Y
    sticky="ew"	    fill=tk.X
    sticky="nsew"	fill=tk.BOTH

.grid() is a powerful geometry manager. It’s often easier to understand than .pack() and is much more flexible than .place(). When you’re creating new Tkinter applications, you should consider using .grid() as your primary geometry manager

.grid() offers much more flexibility than you’ve seen here. For example, you can configure cells to span multiple rows and columns. For more information, check out the Grid Geometry Manager section (https://tkdocs.com/tutorial/grid.html) of the TkDocs(https://tkdocs.com/index.html) tutorial.
'''

#personal test area
#window
window = tk.Tk()
window.title("Dots & Boxes")
#colors 
unclicked_bar_color = "#0DA6AB"
clicked_bar_color = "#1EE0E6"
box_complete_color_by_AI = "#0D80A4"
box_complete_color_by_Human = "#8628AD"
box_color = "#F2F5F7"

#frame
box_container = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
    borderwidth=3
)
box_container.pack()

r = input("number of row? ")
c = input("number of column? ")
r = int(r)
c = int(c)

n = r*c  
if n >= 2:
    n = (n*4) - (((n-2)/2)*3) - (n%2) - 1
else:
    n = 4 

total_bars = n 
r = r + (r + 1)
c = c + (c + 1)

for i in range(0, r):
    for j in range(0, c):
        if i%2 == 0 and j%2 == 1:
            #horizontal bar
            horizontal_bar = tk.Button(
                master=box_container,
                text=str(total_bars),
                fg= clicked_bar_color,
                bg= unclicked_bar_color,
                width="8",
                height="1"
            )
            horizontal_bar.grid(row=i, column=j, sticky="nw", pady=1)
            total_bars -= 1
        elif i%2 == 1 and j%2 == 0:
            #vertical bar 
            vertical_bar = tk.Button(
                master=box_container,
                text=str(total_bars),
                fg= clicked_bar_color,
                bg= unclicked_bar_color,
                width="1",
                height="4"
            )
            vertical_bar.grid(row=i, column=j, sticky="w", padx=2)
            total_bars -= 1
        elif i%2==1 and j%2==1:
            #box
            box = tk.Label(master=box_container, bg=box_color, fg="white")
            box.grid(row=i, column=j, sticky="wnes", padx=1)
        
            

#without mainloop, nothing will be shown
window.mainloop()
#window.destroy()