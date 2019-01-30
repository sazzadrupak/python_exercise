# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        # TODO: Change the title of the main window to be "BMI calculator"

        self.__mainwindow.title('BMI calculator')
        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        self.__mainwindow.geometry("400x400")  # set the width and height of main window
        self.__mainwindow.resizable(0, 0)  # set the main window not resizable
        Label(self.__mainwindow, text="Weight: ").grid(row=0)  # add label to weight at row 0
        Label(self.__mainwindow, text="Height: ").grid(row=1)  # add label form height at row 1

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow, width=30)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow, width=30)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow, text='Calculate', bg="green", fg='white',
                                         command=self.calculate_BMI)
        # TODO: Create a Label that will show the decimal value of the BMI
        # after it has been calculated.
        self.__result_text = Label(self.__mainwindow, text="")
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="")
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text='Stop', bg="red", fg='white', command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=1)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2, column=0)
        self.__stop_button.grid(row=2, column=1, columnspan=1)
        self.__result_text.grid(row=3, columnspan=2)
        self.__explanation_text.grid(row=4, columnspan=2)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text.

            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text.
        """
        try:
            if int(self.__weight_value.get()) > 0 and int(self.__height_value.get()) > 0:
                result = float(int(self.__weight_value.get()) / ((int(self.__height_value.get()) * 0.01) ** 2))

                self.__result_text.config(text="{:.2f}".format(result))

                if result > 25:
                    self.__explanation_text.config(text="You are overweight.")
                elif 18.5 <= result <= 25:
                    self.__explanation_text.config(text="Your weight is normal.")
                else:
                    self.__explanation_text.config(text="You are underweight.")

            else:
                self.reset_fields()
                self.__explanation_text.config(text="Error: height and weight must be positive.")

        except ValueError:
            self.__explanation_text.config(text="Error: height and weight must be numbers.")

    # TODO: Implement this method.
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__height_value.delete(0, 'end')
        self.__weight_value.delete(0, 'end')
        self.__result_text.config(text='')

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
