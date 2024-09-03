import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello, World!")

# Create a heading label
heading = tk.Label(window, text="Welcome to my app!", font={"Arial", 24})
heading.pack(pady=10)

# Function to be called when the count button is clicked
count = 0
def handle_count_button_press(event):
    global count
    count += 1
    button1.config(text=f"Counter {count} times")

# Create the count button
button1 = tk.Button(text="Counted 0 times")
button1.bind("<Button-1>", handle_count_button_press)
button1.pack(pady=10)

# Function to be called when the close button is clicked
def handle_close_button_press(event):
    window.destroy()

# Create the close button
button2 = tk.Button(text="Close the app")
button2.bind("<Button-1>", handle_close_button_press)
button2.pack(pady=10)

window.mainloop()