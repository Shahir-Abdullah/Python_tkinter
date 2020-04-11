import tkinter as tk
#window
window = tk.Tk()
window.title("Dots & Boxes")
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
#colors 
unclicked_bar_color = "#0DA6AB"
clicked_bar_color = "#1EE0E6"
box_complete_color_by_AI = "#0D80A4"
box_complete_color_by_Human = "#8628AD"
box_color = "#F2F5F7"
enter_btn_color = "#17B974"

#frame for ui
taskbar_frame = tk.Frame(
    master=window,
    relief = tk.SUNKEN,
    borderwidth=3
)
taskbar_frame.pack()
#label for row entry
lbl_row = tk.Label(master=taskbar_frame, text="Enter Number of Rows : ")
#entry for row
ent_row = tk.Entry(master=taskbar_frame, width=10)
#label for column entry
lbl_col = tk.Label(master=taskbar_frame, text="Enter Number of Columns : ")
#entry for col
ent_col = tk.Entry(master=taskbar_frame, width=10)
#function 
def enter_row_column():

    r = ent_row.get()
    c = ent_col.get()
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
        for j in range(2, c+2):
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
        
#button for row and column number input
enter_button = tk.Button(
    master = taskbar_frame,
    text="Enter",
    bg = enter_btn_color,
    fg = "white",
    command=enter_row_column
)

lbl_row.grid(row=0, column=0, sticky="w", padx=5)
ent_row.grid(row=0, column=1, sticky="w", padx=5)
lbl_col.grid(row=1, column=0, sticky="w", padx=5)
ent_col.grid(row=1, column=1, sticky="w", padx=5)
enter_button.grid(row=2, column=1, sticky="wn", padx=5, pady=10)


#frame for board
box_container = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
    borderwidth=3
)
box_container.pack()

#without mainloop, nothing will be shown
window.mainloop()
#window.destroy()