import tkinter as tk
from time import strftime

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("24 And 12 Hour Clock")
        
        # Clock 
        self.time_label = tk.Label(root, font=("Press Start 2P", 20), bg="black", fg="lime")
        self.time_label.pack(pady=20, padx=20)
        
        # Toggle 
        self.is_24_hour = True  
        self.toggle_button = tk.Button(
            root,
            text="Switch to 12-hour",
            font=("Press Start 2P", 12),
            bg="black",
            fg="green",
            command=self.toggle_format
        )
        self.toggle_button.pack(pady=10)
        
       
        self.update_time()

    def update_time(self):
        """Update the time displayed on the clock."""
        time_format = "%H:%M:%S" if self.is_24_hour else "%I:%M:%S %p"
        current_time = strftime(time_format)
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)  

    def toggle_format(self):
        """Toggle between 24-hour and 12-hour clock formats."""
        self.is_24_hour = not self.is_24_hour
        button_text = "Switch to 24-hour" if not self.is_24_hour else "Switch to 12-hour"
        self.toggle_button.config(text=button_text)


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    app = ClockApp(root)
    root.mainloop()
