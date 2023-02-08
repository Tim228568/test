from kivy.config import Config



#config
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 720)
Config.set("graphics", "height", 800)




from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore





info = JsonStore('info.json')



#info.put('test7', User="Елизовета Чеботарёва", bal=100)
#info.put('test8', User="Григорьева Даша", bal=100)
#info.put('test9', User="Юдина Вера", bal=100)
#info.put('test10', User="Выборов Даниниил", bal=100)




why = 0
sumn = 0

prof=["test", "test1", "test2", "test3", "test4", "test5", "test", "test7", "test8", "test9", "test10"]

user = info.get(prof[why])["User"]
count = info.get(prof[why])["bal"]

print("У {0}: {1}СШ".format(info.get(prof[why])["User"], info.get(prof[why])["bal"]))  

def on_text(instance, value):
    global sumn
    sumn = value     


class Application(App):
    global count 

    def addnum(self, instance):
        global count
        global sumn
        #self.чтоменяем.какой аргумент
        self.label.text = str(int(count) + int(sumn))+" СШ"
        count = int(count) + int(sumn)
        
        info.put(prof[why], User=info.get(prof[why])["User"], bal=count)
        #print(sumn)
        #print(count)
        #f.read()
        

    def renum(self, instance):
        global count
        global sumn
        #self.чтоменяем.какой аргумент
        self.label.text = str(int(count) - int(sumn))+" СШ"
        count = int(count) - int(sumn)
        
        info.put(prof[why], User=info.get(prof[why])["User"], bal=count)


    def nextn(self, instance):
        global why
        global count
        global sumn
        
        why = why + 1
        print(why)
        print("У {0}: {1}СШ".format(info.get(prof[why])["User"], info.get(prof[why])["bal"]))  
        self.label.text = str(info.get(prof[why])["bal"])+" СШ"
        self.label2.text = str(info.get(prof[why])["User"])
        
        count = 0
        
        
        
    def backn(self, instance):
        global why
        global count
        global sumn
        
        why = why - 1
        print(why)
        print("У {0}: {1}СШ".format(info.get(prof[why])["User"], info.get(prof[why])["bal"]))  
        self.label.text = str(info.get(prof[why])["bal"])+" СШ"
        self.label2.text = str(info.get(prof[why])["User"])

        count = 0
        












    def build(self):
    
        global count
        global sumn
        global user
        
        grid = GridLayout(rows = 2)
        grid2 = GridLayout(rows = 2)
        grid3 = GridLayout(rows = 2)
        grid4 = GridLayout(cols = 2)
        grid5 = GridLayout(rows = 3)
        grid6 = GridLayout(rows = 2)
        
        
        
        test = 3
        #виджиты
        my_but = Button(text="+", font_size=30, background_color="cyan", on_press=self.addnum)
        my_but2 = Button(text="-", font_size=30, background_color="cyan", on_press=self.renum)
        self.label2 = Label(text=str(user), font_size=40, ) 
        self.label = Label(text=str(count)+" СШ", font_size=40) 
        summ = TextInput(text=str(sumn), font_size=40)
        summ.bind(text=on_text)
        nextn = Button(text=">", background_color="cyan", font_size=40, on_press=self.nextn)
        backn = Button(text="<", background_color="cyan", font_size=40, on_press=self.backn)
        #добавляем

        grid.add_widget(grid5)
        grid.add_widget(grid3)
        grid3.add_widget(grid4)

        grid5.add_widget(grid2)
        grid5.add_widget(grid6)

        grid6.add_widget(backn)
        grid6.add_widget(nextn)
        
        grid2.add_widget(self.label2)
        grid2.add_widget(self.label)
        
        grid3.add_widget(summ)
        
        grid4.add_widget(my_but)
        grid4.add_widget(my_but2)
        
        
        
        
        
        
        return grid
        
        
        
        
if __name__ == "__main__":
    Application().run()
    