import customtkinter as tk

class Slider(tk.CTkSlider):
    def __init__(self, master, **kwargs):
        self.value_list = kwargs.pop("value_list") # .pop cause not-standard values (any other value) are now allowed

        super().__init__(master, **kwargs)
        self.value_list = self.value_list

        if self.value_list is not None:
            self.configure(command=self.set_value)
            self.set_value(max(self.value_list))

        self.value = (max(self.value_list))

    def set_value(self, curval):
        curval = get_closest_num(curval, self.value_list)
        if curval in self.value_list:
            self.set(curval)
            self.value = curval

    def set_value_list(self, value_list):
        self.value_list = value_list

def get_closest_num(num, value_list):
    closest_num = None
    min_diff = float('inf')  # Inizializza con un valore molto grande

    for val in value_list:
        diff = abs(num - val)
        if diff < min_diff:
            min_diff = diff
            closest_num = val
    return closest_num