# FOIL Method App

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from sympy import Symbol
from colorama import Back, Style 

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "FOIL Method"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-math,LLC ©"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "FOIL Method"
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "FOIL"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            
""")


#FOIL
Builder.load_string("""
<FOIL>
    id:FOIL
    name:"FOIL"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "FOIL Method"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        list_of_steps.clear_widgets()            
                    
            TextInput:
                id: entry
                text: entry.text
                multiline: False
                hint_text: "(ax + b)(cx + d)"
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                
            Button:
                markup: True
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    FOIL.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class FOIL(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(FOIL, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = sm.previous()
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            a = entry.lower()
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace(")*(",")(")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**","^")
            a = a.replace("( - ","(-")
            a = a.replace("*"," * ")
            
            # Split string method to Highlight each step in green before evaluation
            a_list = a.replace(")("," ").replace("(","").replace(")","")
            a_list = a_list.split(" ")
            print(a_list)
            
            print()
            print("Expression entered:  ",a)
            print()
            
            self.ids.list_of_steps.add_widget(Label(text= "Expression Entered: " + a ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            x = Symbol('x')
            a = a.replace("x","*x")
            
            i = 0
            if a.count("(") == a.count(")"):
            # String Method to find FIRST
                #print("FIRST")
                while i < 1:
                    #print(a)
                    first_left_par = a.find("(")
                    first_right_par = a.find(")")
                    second_left_par = a.rfind("(")
                    second_right_par = a.rfind(")")
                    if a == " / ":
                        print("Invalid Input, no division in or outside of parentheses for Foil Methed")
                        break
                    if a == " * ":
                        print("Invalid Input, no multiplication within parentheses for Foil Method")
                        break
                    
                    right_par_left_side = a.find(")")
                    #print('right_par_left_side',right_par_left_side)
                    left_par_left_side = a[:right_par_left_side].rfind("(")
                    #print('left_par_left_side',left_par_left_side)
                    left_par_range = a[left_par_left_side:right_par_left_side+1]
                    #print('left_par_range: ',left_par_range)
                    
                    j = 0
                    while j < 1:
                        if left_par_range == " + " or "+": #  Find Add Sign
                            first_sign = left_par_range.rfind("+")
                            if first_sign == -1:
                                break
                            #sign = left_par_range.rfind("-")
                            #print("add_sign index: ",first_sign)
                            First_left = a[left_par_left_side+1:first_sign-1]
                            print("First_left",First_left)
                            if First_left == "*x":
                                First_left = "1*x"
                            next_par_range = a[right_par_left_side+1:]
                            #print('next_par_range',next_par_range)
                            left_par_right_side = next_par_range[:].find("(")
                            #print('next_par index',left_par_right_side)
                            right_par_right_side = next_par_range[:].find(")") #First Right Par
                            #print('right_par_right_side',right_par_right_side)
                            first_space_index = next_par_range[:].find(" ")
                            #print('first_space_index',first_space_index)
                            First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                            print('First_right',First_right)# Use for Highlight
                            if First_right == "*x ":
                                First_right = "1*x"
                            #print()
                            #print("First Type ",type(First))
                            FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                            print()
                            First = First_left + " * " + First_right
                            First = First.replace("+-","-").replace("^","**")
                            #print("First Type ",type(First))
                            #First = sympify(First)
                            #print('type',type(First))
                            First = str(First).replace("^","**")
                            print("First",First)
                            First_evaled = str(eval(First))
                            First = str(First).replace("**","^").replace("*-"," * -")
                            
                            FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = 60, size_hint_y= None, height=100))

                            print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)   
                            print()
                            #print('                  ',First_evaled)
                            highlight_first = First_evaled.replace("**","^").replace("*","").replace("-+","-")
                            print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                            
                            FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                            self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = 60, size_hint_y= None, height=100))
                            
                            print()
                            self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
                            print()
                            
                            break
                    if first_sign == -1: #  Find Minus Sign
                        first_sign = left_par_range.rfind("-")
                        #sign = left_par_range.find("+")
                        #print("minus_sign index: ",first_sign)
                        First_left = a[left_par_left_side+1:first_sign-1]
                        if First_left == "*x":
                            First_left = "-1*x"
                        #print('First_left',First_left) # Use for Highlight
                        next_par_range = a[right_par_left_side+1:]
                        #print('next_par_range',next_par_range)
                        left_par_right_side = next_par_range[:].find("(")
                        #print('next_par index',left_par_right_side)
                        right_par_right_side = next_par_range[:].find(")") #First Right Par
                        #print('right_par_right_side',right_par_right_side)
                        first_space_index = next_par_range[:].find(" ")
                        #print('first_space_index',first_space_index)
                        First_right = next_par_range[left_par_right_side+1:first_space_index+1]
                        if First_right == "*x":
                            First_right = "-1*x"
                        #print('First_right',First_right)# Use for Highlight
                        #print()
                        First = First_left + " * " + First_right
                        print('FIRST                ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")")         #print("First Type ",type(First))
                        FIRST_DISPLAY = "FIRST: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_DISPLAY , markup=True, font_size = 60, size_hint_y= None, height=100))

                        #print('type',type(First))
                        First = str(First).replace(" ","").replace("+-","-").replace('--',"+").replace("-+","-").replace("^","**")
                        #x,y,z = symbols('x,y,z')
                        First_evaled = str(eval(First))
                        print()
                        First = str(First).replace("**","^").replace("*-"," * -")
                        First_evaled = First_evaled.replace("**","^")
                        
                        FIRST_MULTIPLY = "Multiply: " + First.replace("*x","x").replace("**","^").replace("*"," * ") + " = " + '[color=33CAFF]' + First_evaled.replace("*x","x").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_MULTIPLY , markup=True, font_size = 60, size_hint_y= None, height=100))

                        print("Multiply:            ", First.replace("*x","x").replace("**","^").replace("*"," * ")," = ",Back.GREEN,First_evaled,Style.RESET_ALL)  
                        print()
                        #print('                  ',First_evaled)
                        highlight_first = First_evaled.replace("**","^").replace("*","")
                        #print()
                        print('Expression:          ',Back.BLUE,highlight_first,Style.RESET_ALL)
                        
                        FIRST_EXPRESSION = 'Expression: ' + '[color=33CAFF]' + highlight_first + "[/color]"
                        self.ids.list_of_steps.add_widget(Label(text= FIRST_EXPRESSION , markup=True, font_size = 60, size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                        
                        print()
                        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                        print()
                            
                        break
                    i = i + 1
            # String method for OUTSIDE
                i = 0
                while i < 1:
                    if next_par_range == "+" or  "-":
                        sign_index = next_par_range.find("+")
                        if sign_index == -1:
                            sign_index = next_par_range.rfind("-")
                        #print('sign_index',sign_index)
                    Outside_right = next_par_range[sign_index:right_par_right_side]
                    Outside_right = Outside_right.replace("+","").replace(" ","").strip()
                    #print("Outside_right",Outside_right)
                    if Outside_right == "*x":
                        Outside_right = "1*x"
                    elif Outside_right == "+ *x":
                        Outside_right = "1*x"
                    elif Outside_right == "- *x":
                        Outside_right = "-1*x"
                    Outside = First_left + " * " + Outside_right
                    print('OUTSIDE              ',"(" + Back.GREEN + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    OUTSIDE_DISPLAY = "OUTSIDE: (" + '[color=33CAFF]' + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_DISPLAY , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                    evaled_Outside = str(Outside).replace("^","**")
                    evaled_Outside = eval(evaled_Outside)
                    Outside = Outside.replace("^","**")
                    evaled_Outside = str(evaled_Outside).replace("**","^")
                    print()
                    print("Multiply:            ",Outside.replace("**","^").replace("*x","x")," = ",Back.GREEN,evaled_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_MULTIPLY = "Multiply: " + Outside.replace("**","^").replace("*x","x") + " = " + '[color=33CAFF]' + evaled_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_MULTIPLY , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                    #print()
                    #print('evaled_Outside',evaled_Outside)
                    #print()
                    highlight_Outside = str(evaled_Outside).replace(" ","").replace("**","^").replace("*","").replace("-"," - ").strip()
                    
                    if highlight_Outside[0] != "-":
                        highlight_Outside = " + " + highlight_Outside
                    print()
                    print("Expression:          ",Back.BLUE,highlight_first,Style.RESET_ALL,Back.GREEN,highlight_Outside,Style.RESET_ALL)
                    
                    OUTSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]'  + highlight_first + highlight_Outside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= OUTSIDE_HIGHLIGHT , markup=True, font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    
                    break
            
            # String Method for INSIDE
                i = 0
                while i < 1:        
                    INSIDE_left = left_par_range[first_sign:right_par_left_side]
                    INSIDE_left = INSIDE_left.replace("^","**")
                    print(INSIDE_left)
                    if INSIDE_left == "+ *x":
                        INSIDE_left = "1*x"
                    elif INSIDE_left == "- *x":
                        INSIDE_left = "-1*x"
                    Inside_sign = left_par_range.find("+")
                    if Inside_sign == -1:
                        Inside_sign = left_par_range.rfind("-")
                        
                    #print("INSIDE_left",INSIDE_left) 
                    #print("Inside_sign index",Inside_sign)
                    Inside_sign_right_side = next_par_range.find("+")
                    if Inside_sign_right_side == -1:
                        Inside_sign_right_side = next_par_range.rfind("-")
                    print('INSIDE               ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + Back.GREEN + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Style.RESET_ALL + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    
                    INSIDE_DISPLAY = "INSIDE (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + '[color=33CAFF]' + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[/color]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_DISPLAY , markup=True, font_size = 60, size_hint_y= None, height=100))

                    Inside =  INSIDE_left + " * " + First_right
                    Inside = Inside.replace("^","**")
                    if Inside == "*x":
                        Inside = "1*x"
                    print()
                    Inside_evaled = str(eval(Inside)).replace(" ","").replace("**","^").replace("+"," +").strip()
                    Inside = Inside.replace("**","^")
                    Inside_evaled = str(Inside_evaled).replace("**","^")
                    Inside_evaled = Inside_evaled.replace("+-","-")
                    print("Multiply:            ",Inside.replace("*x","x").replace("**","^")," = ",Back.GREEN,Inside_evaled,Style.RESET_ALL)
                    print()
                    
                    INSIDE_MULTIPLY = "Multiply: " + Inside.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Inside_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_MULTIPLY , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                    #print("Inside_evaled",Inside_evaled)
                    highlight_Inside = Inside_evaled.replace("*","").replace(" ","")

                    if highlight_Inside[0] != "-":
                        highlight_Inside = " + " + highlight_Inside
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,Style.RESET_ALL,Back.GREEN,highlight_Inside,Style.RESET_ALL)
                    
                    INSIDE_HIGHLIGHT = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= INSIDE_HIGHLIGHT , markup=True, font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()
                    break
                
            # String Method for LAST
                i = 0 
                while i < 1:
                    print('LAST                 ',"(" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + Back.GREEN + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + Style.RESET_ALL + ")")         #print("First Type ",type(First))
                    print()
                    
                    LAST_DISPLAY = "LAST: (" + str(a_list[0]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[1:3]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")(" + str(a_list[3]).replace("[","").replace("]","").replace("'","") + '[color=33CAFF]' + str(a_list[4:]).replace("[","").replace("]","").replace("'","").replace("+"," + ").replace("-"," - ").replace(",","") + '[/color]' + ")"
                    self.ids.list_of_steps.add_widget(Label(text= LAST_DISPLAY , markup=True, font_size = 60, size_hint_y= None, height=100))

                    Last = INSIDE_left + " * " + Outside_right 
                    Last = Last.replace("^","**")
                    if Last == "*x":
                        Last = "1*x"
                    Last_evaled = str(eval(Last)).replace(" ","").replace("**","^").replace("-","- ").strip()
                    Last = Last.replace("^","**")
                    Last_evaled = str(Last_evaled).replace("**","^")
                    print("Multiply:            ",Last.replace("*x","x").replace("**","^")," = ",Back.GREEN,Last_evaled,Style.RESET_ALL)
                    print()
                    #print('Last_evaled',Last_evaled)
                    
                    LAST_MULTIPLY = "Multiply: " + Last.replace("*x","x").replace("**","^") + " = " + '[color=33CAFF]' + Last_evaled + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_MULTIPLY , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                    highlight_Last = Last_evaled.replace("*","")#.replace("-","- ")
            
                    if highlight_Last[0] != "-":
                        highlight_Last = " + " + highlight_Last
            
                    print("Expression:         ",Back.BLUE,highlight_first,highlight_Outside,highlight_Inside,Style.RESET_ALL,Back.GREEN,highlight_Last,Style.RESET_ALL)
                    LAST_EXPRESSION = "Expression: " + '[color=33CAFF]' + highlight_first + highlight_Outside + highlight_Inside + highlight_Last + '[/color]'
                    self.ids.list_of_steps.add_widget(Label(text= LAST_EXPRESSION , markup=True, font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                    print()
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print()        
                    break
                
                FOIL = str(First_evaled) + "+" + str(evaled_Outside) + "+" + str(Inside_evaled) + "+" + str(Last_evaled)
                FOIL = FOIL.strip().replace("**","^").replace(" ","").replace("+-","-").replace("+"," + ").replace("-"," - ").replace("*","")
                print("Expression FOILed:  ",Back.BLUE,FOIL,Style.RESET_ALL)
                EXPRESSION_FOLIED = '[color=33CAFF]' + FOIL + '[/color]'
                self.ids.list_of_steps.add_widget(Label(text= "Expression FOILed:  ", markup=True, font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= EXPRESSION_FOLIED , markup=True, font_size = 60, size_hint_y= None, height=100))
                print()
                self.ids.list_of_steps.add_widget(Label(text= "Next, combine like terms" , markup=True, font_size = 60, size_hint_y= None, height=100))
                print("Next, combine like terms")
                print()
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' , markup=True, font_size = 60, size_hint_y= None, height=100))
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()  
                
                First_evaled = str(First_evaled).replace("^","**")
                evaled_Outside = "+" + str(evaled_Outside).replace("^","**")
                Inside_evaled =  "+" + str(Inside_evaled).replace("^","**")
                Last_evaled =  "+" + str(Last_evaled).replace("^","**")
                First_evaled =  str(First_evaled).replace("+-","-")
                evaled_Outside = str(evaled_Outside).replace("+-","-")
                Inside_evaled =   str(Inside_evaled).replace("+-","-")
                Last_evaled =  str(Last_evaled).replace("+-","-")
                
                #print("aLL CURRENTLY    ",First_evaled," ",evaled_Outside," ",Inside_evaled," ",Last_evaled)
                answer = ""
                combine_evaled_FOIL = ""
                combine_evaled_FO = ""
                combine_evaled_IL = ""
                combine_evaled_FI = ""
                combine_evaled_OL = ""
                combine_evaled_FL = ""
                combine_evaled_OI = ""
            # Combine Like Terms if all can combine
            
                
            #Combine like Terms
            #First evaled, check for if Exponent, Variable, Integer
                First_evaled = First_evaled.replace("**","^")
                evaled_Outside = evaled_Outside.replace("**","^")
                Inside_evaled = Inside_evaled.replace("**","^")
                Last_evaled = Last_evaled.replace("**","^")
                
                exponent_First_evaled = " "
                variable_First_evaled = " "
                integer_First_evaled = " "
                
                exponent_evaled_Outside = " "
                variable_Outside_evaled = " "
                integer_evaled_Outside = " "
                
                exponent_Inside_evaled = " "
                variable_Inside_evaled = " "
                integer_Inside_evaled = " "
                
                exponent_Last_evaled = " "
                variable_Last_evaled = " "
                integer_Last_evaled = " "
                
                non_combine = 0
                
                i = 0
                while i < 1: #Highlight each possible combo
                    if First_evaled.count("^") == 1:
                        exponent_First_evaled = First_evaled.replace("^","**")
                        print(First_evaled.replace("*",""),"is an exponent")
                        carrot = First_evaled.find("^")
                        exponent_First = First_evaled[carrot+1:]
                        print("exponent_First",exponent_First)
                        
                    if evaled_Outside.count("^") == 1:
                        exponent_evaled_Outside = evaled_Outside.replace("^","**")
                        print(evaled_Outside, "Its an exponent")
                        carrot = evaled_Outside.find("^")
                        exponent_Outside = evaled_Outside[carrot+1:]
                        print("exponent_First",exponent_Outside)
                        
                    if Inside_evaled.count("^") == 1:
                        exponent_Inside_evaled = Inside_evaled.replace("^","**")
                        print(Inside_evaled,"Its an exponent")
                        carrot = Inside_evaled.find("^")
                        exponent_Inside = Inside_evaled[carrot+1:]
                        print("exponent_First",exponent_Inside)
                        
                    if Last_evaled.count("^") == 1:
                        exponent_Last_evaled = Last_evaled.replace("^","**")
                        print(Last_evaled,"Its an exponent")
                        carrot = Last_evaled.find("^")
                        exponent_Last = Last_evaled[carrot+1:]
                        print("exponent_First",exponent_Last)
                    
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " " and exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print("1Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + "),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("*","").replace("**","^"),Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled)).replace("**","^").replace("**","^") + '[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if exponent_First_evaled != " " and exponent_evaled_Outside  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print()
                        if exponent_First_evaled[-1] == exponent_evaled_Outside[-1]:
                            print("2Combine terms:      ",Back.BLUE,First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Style.RESET_ALL,Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "),Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*",""),evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     ",Back.BLUE,str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," "),Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Inside_evaled[-1]:
                            print("3Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+ '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_First_evaled != " " and exponent_Last_evaled  != " ":
                        print()
                        print("exponent_First_evaled",exponent_First_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("4Combine terms: "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: " + '[color=33CAFF]' + First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ") + '[/color]' + evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_First_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: " + '[color=33CAFF]' + str(eval(exponent_First_evaled +" + "+ exponent_evaled_Outside)).replace("**","^").replace("*"," ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Inside_evaled  != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("5Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Inside_evaled)).replace("*","").replace("**","^")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_evaled_Outside != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_evaled_Outside",exponent_evaled_Outside)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("6Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+ '[color=33CAFF]' +evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' +Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[color=33CAFF]' + Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ") + '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+ '[color=33CAFF]' +str(eval(exponent_evaled_Outside +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    if exponent_Inside_evaled != " " and exponent_Last_evaled != " ":
                        print()
                        print("exponent_Inside_evaled",exponent_Inside_evaled)
                        print("exponent_Last_evaled",exponent_Last_evaled)
                        print()
                        if exponent_First_evaled[-1] == exponent_Last_evaled[-1]:
                            print("7Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                            COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            print("Terms Combined:     "+Back.BLUE+str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                            COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]' + str(eval(exponent_Inside_evaled +" + "+ exponent_Last_evaled)).replace("*","").replace("**","^")+ '[/color]'
                            self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                            print()
                            non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 1 and First_evaled.count("^") == 0:
                        variable_First_evaled = First_evaled
                        print("Its a variable F"+variable_First_evaled)
                    if evaled_Outside.count("x") == 1 and evaled_Outside.count("^") == 0:
                        variable_Outside_evaled = evaled_Outside
                        print("Its a variable O"+variable_Outside_evaled)
                    if Inside_evaled.count("x") == 1 and Inside_evaled.count("^") == 0:
                        variable_Inside_evaled = Inside_evaled
                        print("Its a variable I"+variable_Inside_evaled)
                    if Last_evaled.count("x") == 1 and Last_evaled.count("^") == 0:
                        variable_Last_evaled = Last_evaled
                        print("Its a variable L"+variable_Last_evaled)
            
                    if variable_First_evaled != " " and variable_Outside_evaled  != " " and variable_Inside_evaled != " " and variable_Last_evaled != " ":
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+ '[/color]' 
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled +" + "+ variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if variable_First_evaled != " " and variable_Outside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Outside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_First_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_First_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Inside_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Outside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Outside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Outside_evaled +" + "+ variable_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if variable_Inside_evaled != " " and variable_Last_evaled != " " :
                        print()
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(variable_Inside_evaled +" + "+ variable_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    non_combine = non_combine + 1
                    break
            
                i = 0
                while i < 1:
                    if First_evaled.count("x") == 0 and First_evaled.count("^") == 0:
                        integer_First_evaled =  First_evaled
                        print("Its an integer F")
                    if evaled_Outside.count("x") == 0 and evaled_Outside.count("^") == 0:
                        integer_evaled_Outside =  evaled_Outside
                        print("Its an integer O")
                    if Inside_evaled.count("x") == 0 and Inside_evaled.count("^") == 0:
                        integer_Inside_evaled =  Inside_evaled
                        print("Its an integer I")
                    if Last_evaled.count("x") == 0 and Last_evaled.count("^") == 0:
                        integer_Last_evaled =  Last_evaled
                        print("Its an integer L")
                      
                    if integer_First_evaled != " " and integer_evaled_Outside  != " " and integer_Inside_evaled != " " and integer_Last_evaled != " ":
                        print("FOIL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside +" + "+ integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","").replace("**","^")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                        break
                    if integer_First_evaled != " " and integer_evaled_Outside != " " :
                        print()
                        print("FO")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_evaled_Outside)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Inside_evaled != " " :
                        print()
                        print("FI")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_First_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("FL")
                        print("Combine terms:      "+Back.BLUE+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Style.RESET_ALL+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+'[color=33CAFF]'+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[/color]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_First_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Inside_evaled != " " :
                        print()
                        print("OI")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- "))
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_evaled_Outside != " " and integer_Last_evaled != " " :
                        print()
                        print("OL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+Back.BLUE+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+'[color=33CAFF]'+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_evaled_Outside +" + "+ integer_Last_evaled)).replace("*","")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_evaled_Outside +" + "+ integer_Inside_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    if integer_Inside_evaled != " " and integer_Last_evaled != " " :
                        print()
                        print("IL")
                        print("Combine terms:      "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Back.BLUE+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Style.RESET_ALL)        
                        COMBINE_TERMS = "Combine terms: "+First_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ")+evaled_Outside.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[color=33CAFF]'+Inside_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+Last_evaled.replace(" ","").replace("**","^").replace("*","").replace("+"," + ").replace("-","- ")+'[/color]'  
                        self.ids.list_of_steps.add_widget(Label(text= COMBINE_TERMS , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        print("Terms Combined:     "+Back.BLUE+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*"+"")+Style.RESET_ALL)
                        COMBINED_TERMS_EVALED = "Terms Combined: "+'[color=33CAFF]'+str(eval(integer_Inside_evaled +" + "+ integer_Last_evaled)).replace("*","")+'[/color]'
                        self.ids.list_of_steps.add_widget(Label(text= COMBINED_TERMS_EVALED , markup=True, font_size = 60, size_hint_y= None, height=100))
                        print()
                        non_combine = non_combine - 1
                    non_combine = non_combine + 1
                    break
                
                if non_combine == 3:
                    print("No terms to combine")
                    self.ids.list_of_steps.add_widget(Label(text= "No terms to combine" , markup=True, font_size = 60, size_hint_y= None, height=100))
                    
                exponents_evaled_list = [exponent_First_evaled,exponent_evaled_Outside,exponent_Inside_evaled,exponent_Last_evaled]
                #print("exponents_evaled_list",exponents_evaled_list)
                #print()
                add_up_exponents = exponent_First_evaled + exponent_evaled_Outside + exponent_Inside_evaled + exponent_Last_evaled
                add_up_exponents = add_up_exponents.replace(" ","").replace("**","^")
                combined_exponents = ""
                if add_up_exponents.count("^") > 0:
                    add_up_exponents = add_up_exponents.replace("^","**").replace(" ","")
                    combined_exponents = str(eval(add_up_exponents)).replace("**","^")
                #print(combined_exponents.replace("**","^").replace("*",""))
                
                First_evaled_exp_index = exponent_First_evaled.find("^")
                #print("First_evaled_exp_index",First_evaled_exp_index)
                
                #print()
                variables_evaled_list = [variable_First_evaled,variable_Outside_evaled,variable_Inside_evaled,variable_Last_evaled]
                #print("variables_evaled_list",variables_evaled_list)
                #print()
                add_up_variables = variable_First_evaled + variable_Outside_evaled + variable_Inside_evaled + variable_Last_evaled
                add_up_variables = add_up_variables.strip().replace(" ","")
                combined_variables = ""
                if add_up_variables.count("x") > 0:
                    combined_variables = str(eval(add_up_variables))
                #print("combined_variables",combined_variables)
                #print()
                
                #integers_evaled_list = [integer_First_evaled,integer_evaled_Outside,integer_Inside_evaled,integer_Last_evaled]
                #print("integers_evaled_list",integers_evaled_list)
                #print()
                add_up_integers = integer_First_evaled + integer_evaled_Outside + integer_Inside_evaled + integer_Last_evaled
                #print("add_up_integers length",len(add_up_integers.replace(" ","")))
                combined_integers = ""
                add_up_integers = add_up_integers.strip().replace(" ","")
                if len(add_up_integers.replace(" ","")) != 0:
                   combined_integers = str(eval(add_up_integers))
                #print("combined_variables",combined_integers)
                
                FINAL_ANSWER = (str(combined_exponents) + "+" + str(combined_variables) + "+" + str(combined_integers)).replace("*","").replace("++","")
                print("FINAL_ANSWER: ",FINAL_ANSWER)
                if FINAL_ANSWER[-1] == "+" or FINAL_ANSWER[-1] == "-":
                    FINAL_ANSWER = FINAL_ANSWER[:-1]
                FINAL_ANSWER = FINAL_ANSWER.replace("+-","-").replace("-"," - ").replace("+"," + ").replace("*","")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                print("Answer in order:    ",FINAL_ANSWER)
                self.ids.list_of_steps.add_widget(Label(text= '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Final Answer: " + FINAL_ANSWER.replace("*","") ,font_size = 60, size_hint_y= None, height=100))
                
            else:
                print("Parentheses Unbalanced")
            
            
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass 
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(FOIL(name="FOIL"))     
sm.current = "Homepage"   


class FOIL(App):
    def build(app):
        return sm

if __name__ == '__main__':
    FOIL().run()
