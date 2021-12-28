from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
#from colorama import Back, Style 

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
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared PEMDAS Calculator"
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
        do_scroll_y: True# Slope intercept form
# y = mx + b
# domain and range
# graph

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

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
            height: 200
            text: "KSquared-math,LLC ©"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Slope Intercept Calculator"
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
                text: "Domain and Range"
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Domain_and_Range"
                    root.manager.transition.direction = "left"
                    
            Button:
                text: "Graph"
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Graph"
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

#Domain_and_Range 
Builder.load_string("""
<Domain_and_Range>
    id:Domain_and_Range
    name:"Domain_and_Range"
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
                text: "Domain and Range"
                    
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
                        y.text = ""
                        domain.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "y = mx + b"       
                                                        
            TextInput:
                id: y
                text: y.text
                multiline: False
                hint_text: "y ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                    
            TextInput:
                id: domain
                text: domain.text
                multiline: False
                hint_text:"Domain = min,max,sequence"
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10  
                
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Domain_and_Range.steps(y.text + "&" + domain.text)  
                
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

#Graph
Builder.load_string("""
<Graph>:
    id: Graph
    name: "Graph"
    
    BoxLayout:
        id:box
        size_hint_y: .8
        pos_hint: {"top":1}
        
    BoxLayout:
        size_hint_y: .2
        TextInput:
            id: y
            multiline: False
            hint_text: "f(x) ="
            text: y.text
            
        TextInput:
            id: domain
            multiline: False
            hint_text: "Domain = 1,2,3,4,..."
            text: domain.text
            
    BoxLayout:
        size_hint_y: .1
        
        Button:
            text: "Menu"   
            background_color: 0, 0 , 1 , 1
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "right" 
        
        Button:
            text: "Graph"
            background_color: 0, 1 , 0 , 1
            on_release:
                box.clear_widgets()
                Graph.graph(y.text + "?" + domain.text)
                
        Button:
            text: "Clear"
            background_color: 1, 0 , 0 , 1
            on_release:
                y.text = "x"
                domain.text = "0"
                box.clear_widgets()
                Graph.graph(y.text + "?" + domain.text)
                y.text = ""
                domain.text = ""
                
""")

class Domain_and_Range(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Domain_and_Range, self).__init__(**kwargs)
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
        entry.replace(" ","")
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        
        try:
            print()
            amp = entry.find("&")
            y = entry[:amp]
            print("y:",y)
            
            self.ids.list_of_steps.add_widget(Label(text= "y = " + y.replace(" ","").replace("y=","").replace("+"," + ").replace("-"," - ") ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            domain = entry[amp+1:]
            print("domain",domain)
            
            domain_comma = domain.find(",")
            comma_count = domain.count(",")
            
            print("domain_comma",domain_comma)
            
            if comma_count == 0 and y.count("x") == 1:
                y = y.replace("x","*" + str(domain))
                print("y = ",y)
                if y[0] == "*":
                    y = y.replace("*","")
                y = y.replace("^","**")
                y = str(eval(y))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(domain) + " | " + str(y) ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif comma_count == 1 and y.count("x") == 1:
                
                empty_domain = []
                for x in range(int(domain[:domain_comma]), int(domain[domain_comma + 1:]) + 1):
                	empty_domain.append(x)
                print("empty_domain",empty_domain) 
                
                i = 0
                range_y = []
                print("loop start")
                print(len(empty_domain))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                while i < len(empty_domain):
                    y_input = str(y).replace("x","*" + str(empty_domain[i]))
                    if y_input[0] == "*":
                        y_input = y_input.replace("*"," ")
                    print("y_input",y_input)
                    y_input = y_input.replace("^","**")
                    y_solved = eval(y_input)
                    print("y_solved",y_solved)
                    range_y.append(y_solved)
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(empty_domain[i]) + " | " + str(y_solved) ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    i = i + 1
                    
                print("range_y",range_y)
                    
            elif comma_count == 2 and y.count("x") == 1:
                print("domain",domain)
                
                domain_list = str(domain).split(",")
                print(domain_list)
                
                sequence_list = []
                for x in range(int(domain_list[0]),int(domain_list[1]),int(domain_list[2])):
                    sequence_list.append(x)
                print("sequence_list",sequence_list)    
                
                if y.count("x") == 1:
                    i = 0
                    range_y = []
                    print("loop start")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    while i < len(sequence_list):
                        y_input = str(y).replace("x","*" + str(sequence_list[i]))
                        if y_input[0] == "*":
                            y_input = y_input.replace("*","")
                        print("y_input",y_input)
                        y_input = y_input.replace("^","**")
                        y_solved = eval(y_input)
                        print("y_solved",y_solved)
                        range_y.append(y_solved)
                        
                        self.ids.list_of_steps.add_widget(Label(text= str(sequence_list[i]) + " | " + str(y_solved) ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                        i = i + 1
                        
                    print("range_y",range_y)
                    
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

class Graph(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        y = [0]
        x = [0]
        
        plt.plot(x,y)
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        
        self.ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
    def graph(self,entry):
        try:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(entry)
            
            ques_index = entry.find("?")
            print("ques_index",ques_index)
            
            func = entry[:ques_index].lower()
            print("func",func)
            
            domain = entry[ques_index+1:]
            print("domain",domain)
            
            y = []
            x = []
            
            domain_list = domain.split(",")
            print("domain_list",domain_list)
            
            i = 0
            while i < len(domain_list):
                function = str(func.replace("x","*" + domain_list[i])).replace("^","**")
                print("function",function)
                
                if function[0] == "*":
                    function = function[1:]
                function_answered = eval(function)
                print("function_answered",function_answered)
                
                x.append(float(domain_list[i]))
                y.append(float(function_answered))
                
                i = i + 1
                
            plt.cla()
            plt.title("f(x) = "+func.replace(" ",""))
            plt.grid(linewidth = 2)
            plt.plot(x,y)
            plt.xlabel("X Axis")
            plt.ylabel("Y Axis")
            
            self.ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
            
        except Exception:
            self.ids.box.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
    
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass 
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Domain_and_Range(name="Domain_and_Range"))     
sm.add_widget(Graph(name="Graph"))   
sm.current = "Homepage"   


class Domain_and_Range(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Domain_and_Range().run()
        
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
                text: "PEMDAS"   
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "PEMDAS"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                size_hint_y: None
                height: 200
                text: "Visit KSquared"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            
""")

Builder.load_string("""
<PEMDAS>
    id:PEMDAS
    name:"PEMDAS"
    
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
                text: "PEMDAS"
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
            
                Button:
                    id: steps
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
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
                hint_text: "Enter expression:"
                multiline: False
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
            
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    PEMDAS.steps(entry.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class PEMDAS(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(PEMDAS, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = "Menu"
            
    layouts = []
    def steps(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        print("entry",entry)
        
        
        try:
            #Parentheses
            a = entry
            a = a.strip()
            a = a.replace(" ","").replace("÷","/").replace("×","*")
            print(a)
            print()
            print("------------------------------")
            print()
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")
            
            print("Expression Entered :      ",a)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            self.ids.list_of_steps.add_widget(Label(text="Expression entered : ", font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= entry, font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            #String Method to look for Parentheses
            if a.count("(") == a.count(")"):
                  i = 0
                  while i < len(a):
                    right_par = a.find(")")
                    left_par = a[:right_par].rfind("(")
                    if right_par and left_par == -1:
                        break
                    range_pars = a[left_par:right_par+1]
                    range_pars = range_pars.replace("^","**")
                    print(range_pars)
                    evaled = eval(range_pars)
                    evaled = str(evaled)
                    print(evaled)
                    range_pars = range_pars.replace("**","^")
                    if a.count("(") and a.count(")") == 0:
                        break
                    print()
                    print()
                    #print("Parentheses to Solve :    ",a[:left_par],Back.GREEN,range_pars,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + range_pars + a[right_par+1:], font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    replaced = a.replace(range_pars,evaled)
                    print()
                    #print("Parentheses Solved :      ",a[:left_par],Back.GREEN,evaled,Style.RESET_ALL,a[right_par+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Parentheses Solved : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:left_par] + evaled + a[right_par+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    i = i + 1 
                    
            else:
                print("Parentheses Unbalanced!")
            
            a = a.replace(" ","")
            a = a.replace("+-","-")
            a = a.replace("-+","-")
            a = a.replace("+"," + ")
            a = a.replace("-"," - ")
            a = a.replace("**", "^")
            a = a.replace("*"," * ")
            a = a.replace("/"," / ")
            a = a.replace(" ^ - ","^-")

            
            #String Method to look for Exponents
            i = 0
            if a.count("^") > 0:
                while i < len(a):
                    carrot = a.find("^")
                    if carrot == -1:
                        break
                    print("carrot at index: ",carrot)
                    exp_right_side = a[carrot:]
                    print("exp_right_side",exp_right_side)
                    exp_right_space = exp_right_side.find(" ")
                    print("exp_right_space",exp_right_space)
                    if exp_right_space == -1:
                        exp_right_space = exp_right_side.rfind("")
                    print("exp_right_space",exp_right_space)
                    exp_right_side = a[carrot:carrot + exp_right_space]
                    print("right_side",exp_right_side)
                    exp_left_space = a[:carrot+1].rfind(" ")
                    print("left_side",exp_left_space)
                    if exp_left_space == -1:
                        exp_left_space = a[:carrot+1].find("")
                        print("left_side",exp_left_space)
                    exponent_range = a[exp_left_space:carrot + exp_right_space+1]
                    print("exp_range",exponent_range)
                    if exponent_range[:] == "-":
                        negative = exponent_range.find("-")
                        print("Negative",negative)
                        carrot_inner = exponent_range.find("^")
                        print("carrot_inner",carrot_inner)
                        exponent_left_range = exponent_range[negative:carrot_inner]
                        print("exponent_left_range",exponent_left_range)
                        exponent_left_sliced = "(" + exponent_left_range + ")"
                        exponent_range = exponent_range.replace(exponent_left_range,exponent_left_sliced)
                        print("exponent",exponent_range)
                    print("Exponent to be solved:",exponent_range)
                    exponent_range = exponent_range.replace("^","**")
                    evaled = str(eval(exponent_range))
                    exponent_range = exponent_range.replace("**","^").replace("(","").replace(")","")
                    replaced = a.replace(exponent_range,evaled)
                    print()
                    print()
                    #print("Exponent to Solve :       ",a[:exp_left_space],Back.GREEN,exponent_range,Style.RESET_ALL,a[carrot + exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + exponent_range + a[carrot + exp_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                    print()
                    #print("Exponent Sovled :         ",a[:exp_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[carrot+exp_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Exponent Solved : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:exp_left_space] + evaled + a[carrot+exp_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    print("",replaced)
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")

                i = i + 1
            
            #String Method to look for Multiplication
            i = 0
            print(a)
            if a.count("*") > 0:
                while i < len(a):
                    a = a.replace(" * ","*")
                    print("mult",a)
                    found_mult = a.find("*")
                    if found_mult == -1:
                        break
                    print(found_mult)
                    mult_right_side = a[found_mult:]
                    print("mult_right_side",mult_right_side)
                    mult_right_space= mult_right_side.find(" ")
                    if mult_right_space == -1:
                        mult_right_space = mult_right_side.rfind("")
                    print("mult_right_found at index:",mult_right_space)
                    mult_left_side = a[:found_mult]
                    print("mult_left_side",mult_left_side)
                    mult_left_space = mult_left_side.rfind(" ")
                    if mult_left_space == -1:
                        mult_left_space = mult_left_side.find("")
                    print("mult_left_found at index:",mult_left_space)
                    mult_range = a[mult_left_space:found_mult + mult_right_space+1]
                    if mult_range == "":
                        break
                    print("mult_range",mult_range)
                    evaled = eval(mult_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("*"," * ")
                    replaced = a.replace(mult_range,evaled)
                    print("replaced",replaced)
                    print("m",a)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"
                    
                    print()
                    print()
                    #print("Multiplication to Solve : ",a[:mult_left_space],Back.GREEN,mult_range,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + mult_range + a[found_mult+mult_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    
                    print()
                    #print("Multiplication Solved :   ", a[:mult_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_mult+mult_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Multiplication Solved : ", font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:mult_left_space] + evaled + a[found_mult+mult_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")
   
                i = i + 1
            
            #String Method to look for Division
            i = 0
            print(a)
            if a.count("/") > 0:
                while i < len(a):
                    a = a.replace(" / ","/")
                    print("div",a)
                    found_div = a.find("/")
                    if found_div == -1:
                        break
                    print(found_div)
                    div_right_side = a[found_div:]
                    print("div_right_side",div_right_side)
                    div_right_space= div_right_side.find(" ")
                    if div_right_space == -1:
                        div_right_space = div_right_side.rfind("")
                    print("div_right_found at index:",div_right_space)
                    div_left_side = a[:found_div]
                    print("div_left_side",div_left_side)
                    div_left_space = div_left_side.rfind(" ")
                    if div_left_space == -1:
                        div_left_space = div_left_side.find("")
                    print("div_left_found at index:",div_left_space)
                    div_range = a[div_left_space:found_div + div_right_space+1]
                    if div_range == "":
                        break
                    print("div_range",div_range)
                    evaled = eval(div_range)
                    print(evaled)
                    evaled = str(evaled)
                    evaled = evaled.replace("/"," / ")
                    replaced = a.replace(div_range,evaled)
                    print("replaced",replaced)
                    print("m",a)
                    
                    if evaled.count("-") == 1:
                        evaled = "(" + evaled + ")"
                    
                    print()
                    print()
                    #print("Division to Solve : ",a[:div_left_space],Back.GREEN,div_range,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + div_range + a[found_div+div_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    
                    print()
                    #print("Division Solved :   ", a[:div_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_div+div_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Division Solved : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:div_left_space] + evaled + a[found_div+div_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")

                i = i + 1
            
            #String Method to look for Addition
            i = 0
            while i < len(a):
                if a.count("+") > 0:
                    a = a.replace(" + ","+")
                    print("add",a)
                    found_add = a.find("+")
                    if found_add == -1:
                        break
                    print('found_add',found_add)
                    add_left = a[:found_add]
                    print('add_left',add_left)
                    add_left_space = add_left.rfind(" ")
                    print('add_left_space',add_left_space)
                    if add_left_space == -1:
                        add_left_space = add_left.find("")
                        print('add_left_space',add_left_space)
                    add_right = a[found_add+1:]
                    print('add_right',add_right)
                    add_right_space = add_right.find(" ")
                    print('add_right_space',add_right_space)
                    if add_right_space == -1:
                        add_right_space = add_right.rfind("")
                        print('add_right_space',add_right_space)
                    add_range = a[add_left_space:found_add+add_right_space+1]
                    if add_range == "":
                        break
                    print('add_range',add_range)
                    evaled = eval(add_range)
                    print('evaled',evaled)
                    evaled = str(evaled)
                    replaced = a.replace(add_range,evaled)
                    print('replaced',replaced)
                    print()
                    print()
                    #print("Addition to Solve :       ",a[:add_left_space],Back.GREEN,add_range,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + add_range + a[found_add+add_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    
                    print()
                    #print("Addition  Solved :        ",a[:add_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_add+add_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Addition Solved : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:add_left_space] + evaled + a[found_add+add_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = replaced
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")

                i = i + 1
            
            #String Method to look for Subtraction
            i = 0 
            while i < len(a):
                if a.count("-") > 0:
                    a = a.replace(" - ","-")
                    print("sub",a)
                    found_sub = a.find("-")
                    if found_sub == -1:
                        break
                    print("found_sub",found_sub)
                    sub_left = a[:found_sub]
                    print("sub_left",sub_left)
                    if sub_left == "":
                        break
                    sub_left_space = sub_left.rfind(" ")
                    if sub_left_space == -1:
                        sub_left_space = sub_left.find("")
                        print("sub_left_space",sub_left_space)
                    sub_right = a[found_sub+1:]
                    print('sub_right',sub_right)
                    sub_right_space = sub_right.find(" ")
                    if sub_right_space == -1:
                        sub_right_space = sub_right.rfind("")
                        print("sub_right_space",sub_right_space)
                    sub_range = a[sub_left_space:found_sub+sub_right_space+1]
                    print("sub_range",sub_range)
                    if sub_range == "":
                        break
                    evaled = eval(sub_range)
                    print("evaled",evaled)
                    evaled = str(evaled)
                    replaced = a.replace(sub_range, evaled)
                    a = replaced
                    print("s",a)
                    print()
                    print()
                    #print("Subtraction to Solve :    ",a[:sub_left_space],Back.GREEN,sub_range,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Step : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + sub_range + a[found_sub+sub_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    
                    print()
                    #print("Subtraction  Solved :     ",a[:sub_left_space],Back.GREEN,evaled,Style.RESET_ALL,a[found_sub+sub_right_space+1:])
                    self.ids.list_of_steps.add_widget(Label(text="Subtraction Solved : " , font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= a[:sub_left_space] + evaled + a[found_sub+sub_right_space+1:], font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    a = a.replace(" ","")
                    a = a.replace("+-","-")
                    a = a.replace("-+","-")
                    a = a.replace("+"," + ")
                    a = a.replace("-"," - ")
                    a = a.replace("**", "^")
                    a = a.replace("*"," * ")
                    a = a.replace("/"," / ")
                    a = a.replace(" ^ - ","^-")

                i = i + 1
            a = a.replace(" ","")
            a = a.replace("e - ","e-")
            
            #print Answer with commas
            a = float(a)
            a = format(a,",")
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()
            print("Answer:                     ",a)
            self.ids.list_of_steps.add_widget(Label(text="Final Answer : ", font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= a, font_size = 60, size_hint_y= None, height=100))


        except Exception:
            try:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                    
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
sm.add_widget(PEMDAS(name="PEMDAS"))
sm.current = "Homepage"   


class Math(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Math().run()
    

