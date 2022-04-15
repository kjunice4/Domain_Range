# domain and range of a given function
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import math
from colorama import Back, Style 
import mpmath as mpmath

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
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics :"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"                 
        
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Domain and Range Calculator"
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
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
            
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 1000
                width: 1000

""")

#Updates 
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
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
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
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
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Domain and Range v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
    
    
""")

#Domain_and_Range Calculator 
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
                text: "f(x) = ax + b"       
                                                        
            TextInput:
                id: y
                text: y.text
                multiline: False
                hint_text: "f(x) ="
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10
                    
            TextInput:
                id: domain
                text: domain.text
                multiline: False
                hint_text:"Domain = min,max,sequence"
                font_size: 75
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

class Domain_and_Range(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Domain_and_Range, self).__init__(**kwargs)
            
    layouts = []
    def steps(self,entry):
        print()
        print("~~~~~~~~~~~~~~~~")
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
            self.ids.list_of_steps.add_widget(Label(text= "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
            domain = entry[amp+1:]
            print("domain",domain)
            
            domain_comma = domain.find(",")
            comma_count = domain.count(",")
            
            print("domain_comma",domain_comma)
            
            if comma_count == 0 and y.count("x") > 0:
                y = y.replace("x","*" + str(domain)).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
                print("y = ",y)
                if y[0] == "*":
                    y = y.replace("*","")
                y = y.replace("^","**")
                y = str(eval(y))
                
                self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= str(domain) + " | " + str(y) ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
            elif comma_count == 1 and y.count("x") > 0:
                
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
                    y_input = str(y).replace("x","*" + str(empty_domain[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
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
                    
            elif comma_count == 2 and y.count("x") > 0:
                print("domain",domain)
                
                domain_list = str(domain).split(",")
                print(domain_list)
                
                sequence_list = []
                for x in range(int(domain_list[0]),int(domain_list[1]),int(domain_list[2])):
                    sequence_list.append(x)
                print("sequence_list",sequence_list)    
                
                if y.count("x") > 0:
                    i = 0
                    range_y = []
                    print("loop start")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Domain | Range" ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "x | y" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    while i < len(sequence_list):
                        y_input = str(y).replace("x","*" + str(sequence_list[i])).replace("+*","+").replace("-*","-").replace("/*","/").replace("(*","(").replace("sqrt","math.sqrt").replace("pi","math.pi").replace("^","**").replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan").replace("csc","mpmath.csc").replace("sec","mpmath.sec").replace("cot","mpmath.cot").replace("log","math.log").replace("e","math.e").replace("smath.ec","mp.sec").replace("math.smath.secc","mp.sec").replace("math.math","math").replace("mp.mp","mp")
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

    
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass 

class updates(Screen):
    pass
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Domain_and_Range(name="Domain_and_Range"))     
sm.add_widget(updates(name="updates"))
sm.current = "Homepage"   


class Domain_and_Range(App):
    def __init__(self, **kwargs):
        super(Domain_and_Range, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Domain_and_Range().run()
