import flet as ft
import math
from math import *

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text
        self.style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))

class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE
        self.color = ft.colors.BLACK

class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.WHITE
        self.color = ft.colors.BLACK

class ActionButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.WHITE
        self.color = "#FF7335"

class EqualsButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = "#FFFFFF"    
        self.color = "#FF7335"

class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()   

        self.result2 = ft.Text(value=" ", color=ft.colors.WHITE, size=10)         
        self.result = ft.TextField(
            read_only=True,
            border_color="#FFFFFF",
            bgcolor="#FFFFFF",
            width=320,            
            text_align="end", 
            text_style=ft.TextStyle(size=30, color="#000000")
        )          
        self.width = 350         
        self.bgcolor = "#9eda96"                  
        self.padding = 15                  
        self.content = ft.Column(     
            controls=[          
                ft.Row(controls=[self.result2], alignment="end"),     
                ft.ResponsiveRow(controls=[self.result], alignment="end"),
               
                ft.Row(
                    controls=[
                        ActionButton(text="AC", button_clicked=self.button_clicked),                        
                        DigitButton(text="+/-", button_clicked=self.button_clicked),  
                        DigitButton(text="0", button_clicked=self.button_clicked),    
                        ActionButton(text="÷", button_clicked=self.button_clicked),                                                      
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="x", button_clicked=self.button_clicked),                                           
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),                                             
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),                                                
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="e", button_clicked=self.button_clicked),
                        DigitButton(text="π", button_clicked=self.button_clicked),
                        DigitButton(text=".", button_clicked=self.button_clicked),                                             
                        ActionButton(text="%", button_clicked=self.button_clicked),      
                    ]
                ),
                ft.Row(
                    controls=[
                        ActionButton(text="x²", button_clicked=self.button_clicked),     
                        ActionButton(text="1/x", button_clicked=self.button_clicked),    
                        ActionButton(text="|x|", button_clicked=self.button_clicked),  
                        EqualsButton(text="=", button_clicked=self.button_clicked),      
                    ]
                )              
            ]
        )

    def button_clicked(self, e):
        data = e.control.data             
        
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "." ):
            if self.result.value == "0" or self.new_operand == True:            
                self.result.value = data
                self.new_operand = False
            else:                
                self.result.value = self.result.value + data

        elif data in ("+", "-", "x", "÷", "|x|", "1/x", "%", "x²"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator)            
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True       

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator)            
            self.reset()     
        elif data in ("e"):
            self.result.value = float(math.e)
        elif data in "π":
            self.result.value = math.pi          
        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)
            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )       
        self.update()                    

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num
        
    def calculate(self, operand1, operand2, operator):
        if operator == "+":            
           return self.format_number(operand1 + operand2)
        elif operator == "-":
            return self.format_number(operand1 - operand2)
        elif operator == "x":
            return self.format_number(operand1 * operand2)       
        elif operator == "x²":
            return self.format_number(operand1 ** 2)       
        elif operator == "1/x":
            return self.format_number(1 / operand1)                     
        elif operator == "%":
            return self.format_number(operand1 / 100)                      
        elif operator == "|x|":            
           return self.format_number(abs(float(operand1)))         
        elif operator == "÷":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)             
    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True
