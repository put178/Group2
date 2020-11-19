import tkinter as tk
from user_interface.active_windows import user_management_window
from user_interface.menu_items import menu_item

class UserManagementMenuItem(menu_item.MenuItem):
    """This class is used to create a button that will bring the user to the user management menu.
    """
    def __init__(self, main_menu, frame):
        """
        Args:
            main_menu ([]): this class must know about the main menu because it knows about the GUI, and we need to alter the GUI's active window
        """
        menu_item.MenuItem.__init__(self, main_menu, frame)

        self.create_button()

    def create_button(self):
        """Creates and places the button for the user management menu item."""

        self.button = tk.Button(self.frame, text="User Management", font=("Helvetica", 15))
        self.button["command"] = self.get_user_management_window

        self.button.pack(fill=tk.X)

    def get_user_management_window(self):
        """This function will hide everything on the active window and display the user management window
        """
        self.gui.active_window.hide()

        self.associated_window = user_management_window.UserManagementWindow(self.gui.master)
        self.gui.active_window = self.associated_window

        self.gui.active_window.show()