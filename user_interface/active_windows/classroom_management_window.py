import tkinter as tk
from user_interface.active_windows import active_window

class ClassroomManagementWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        # //TODO Make the Classroom Management Window
        # The two lines below can be removed once the window starts being made
        label = tk.Label(self.frame, text="Classroom Management")
        label.pack()