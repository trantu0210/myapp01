import flet as ft 
from flet import AppBar, ElevatedButton, Page, Text, View, colors
from flet import *
import page1, page2
from page1 import CalculatorApp
from page2 import CalculatorApp2

def main(page: Page):
    page.title = "Calculator App"   
    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    CalculatorApp(),   
                    ft.Container(
                        content=ft.Row(
                            [     
                                ElevatedButton("Page 2", on_click=lambda _: page.go("/page2")),  
                                ft.Icon(name=ft.icons.MY_LIBRARY_BOOKS_OUTLINED, color="orange" ),  
                                ft.Icon(name=ft.icons.BEACH_ACCESS, color="#089e08")                                                                                                  
                            ]                           
                        )
                    )    
                ]
            )
        )
        if page.route == "/page2":
            page.views.append(
                View(
                    "/page2",
                    [
                        CalculatorApp2(),    
                        ft.Container(
                            content=ft.Row(
                                [   
                                    ElevatedButton("Page1", on_click=lambda _: page.go("/page1")),  
                                    ft.Icon(name=ft.icons.BEACH_ACCESS, color="#089e08", size=20),     
                                    ft.Icon(name=ft.icons.MY_LIBRARY_BOOKS_OUTLINED, color="orange", size=20 )                                                                  
                                ]                           
                            )
                        )                                    
                    ]
                )
            )        
        page.update()
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
ft.app(main)
