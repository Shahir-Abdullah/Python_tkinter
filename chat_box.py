import tkinter as tk 

window = tk.Tk()
#title of the window
window.title("Chatbox")
#resizable and responsive window
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=1, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)
#border effects
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
#colors
label_color = "#E5E8E8"
label_text_color = "#34495E"
btn_color = "#ABB2B9"
frame_color = "#2471A3"
btn_text_color = "#212F3C"

#frame for user 1
frame_user1 = tk.Frame(
    master=window,
    relief=tk.GROOVE,
    bg = frame_color,
    borderwidth=2
)
frame_user1.grid(row=0, column=0, sticky="ne", padx=5, pady=5)
#label for user name
lbl_user1 = tk.Label(
    master = frame_user1,
    text="William M. Buttlicker",
    bg = label_color,
    fg = label_text_color
)
#label for inbox
lbl_inbox = tk.Label(
    master = frame_user1,
    text="Inbox",
    bg = label_color,
    fg = label_text_color
)
#inbox 
inbox_user1 = tk.Text(
    master=frame_user1,
    width="20",
    height="10"
)
#label for write
lbl_write = tk.Label(
    master=frame_user1,
    text="Write :",
    bg = label_color,
    fg = label_text_color
)
#text box for writing 
write_box = tk.Text(
    master = frame_user1,
    width="8",
    height="5"
)
#text send from user 1 to user 2 function
def sendmsgtouser2():
    text = write_box.get("1.0", tk.END)
    write_box.delete("1.0", tk.END) 
    inbox_user2.insert(tk.END, text)
#send button 
btn_send = tk.Button(
    master = frame_user1,
    text="Send",
    bg = btn_color,
    fg= btn_text_color,
    command=sendmsgtouser2
    
)
lbl_user1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
lbl_inbox.grid(row=1, column=0, sticky="w", padx=5, pady=5)
inbox_user1.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
lbl_write.grid(row=3, column=0, sticky="w", padx=5, pady=5)
write_box.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
btn_send.grid(row=5, column=0, sticky="es", padx=5, pady=5)


#user 2 card 
#frame for user 2
frame_user2 = tk.Frame(
    master=window,
    relief=tk.GROOVE,
    bg = frame_color,
    borderwidth=2
)
frame_user2.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
#label for user name
lbl_user2 = tk.Label(
    master = frame_user2,
    text="Dwight Schrute",
    bg = label_color,
    fg = label_text_color
)
#label for inbox
lbl_inbox_2 = tk.Label(
    master = frame_user2,
    text="Inbox",
    bg = label_color,
    fg = label_text_color
)
#inbox 
inbox_user2 = tk.Text(
    master=frame_user2,
    width="20",
    height="10"
)
#label for write
lbl_write_2 = tk.Label(
    master=frame_user2,
    text="Write :",
    bg = label_color,
    fg = label_text_color
)
#text box for writing 
write_box_2 = tk.Text(
    master = frame_user2,
    width="8",
    height="5"
)
#text send from user 2 to user 1 function
def sendmsgtouser1():
    text = write_box_2.get("1.0", tk.END)
    write_box_2.delete("1.0", tk.END)
    inbox_user1.insert(tk.END, text)
#send button 
btn_send_2 = tk.Button(
    master = frame_user2,
    text="Send",
    bg = btn_color,
    fg= btn_text_color,
    command=sendmsgtouser1
    
)
lbl_user2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
lbl_inbox_2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
inbox_user2.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
lbl_write_2.grid(row=3, column=1, sticky="w", padx=5, pady=5)
write_box_2.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
btn_send_2.grid(row=5, column=1, sticky="es", padx=5, pady=5)

#without mainloop, nothing will be shown
window.mainloop()