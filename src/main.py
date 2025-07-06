import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Hello World App")
    root.geometry("300x200")

    # Add autofocus when app is opened
    root.lift()  # Bring window to front
    root.attributes('-topmost', True)  # Make window stay on top temporarily
    root.after_idle(root.attributes, '-topmost', False)  # Remove topmost after idle
    root.focus_force()  # Force focus on the window

    # Create a label with "Hello World" text
    hello_label = ttk.Label(
        root,
        text="Hello World!",
        font=("Arial", 16),
        foreground="blue"
    )

    # Place the label in the center of the window
    hello_label.pack(expand=True)


    # Create a button that shows a message when clicked
    def show_message():
        message_label.config(text="Button clicked!")


    button = ttk.Button(
        root,
        text="Click me!",
        command=show_message
    )
    button.pack(pady=10)

    # Create another label for button feedback
    message_label = ttk.Label(root, text="", font=("Arial", 10))
    message_label.pack()

    # Start the GUI event loop
    root.mainloop()