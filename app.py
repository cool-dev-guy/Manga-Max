from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
# from kivymd.config import Config
# Config.set('graphics', 'resizable', True)
class MangaAppRootLayout(MDBoxLayout):
    def searchUI(self,w):
        
        if self.ids.app_menu_in_h:
            print("j")
            self.ids.app_menu_in.clear_widgets()
            self.ids.app_menu_in.size_hint_x=0.7
            self.ids.app_menu_in.size_hint_y=0.9
            self.ids.app_menu_in.add_widget(MDTextFieldRect(size_hint_x=0.5,size_hint_y= 1,hint_text= 'Empty field',height=self.height,multiline=False,pos_hint= {"center_x": .5, "center_y": .5}))
        else:
            print("ww")
    def search(self,w):
        print("search")
            
class MangaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return MangaAppRootLayout()

    def on_press_button(self):
        print('You pressed the button!')

if __name__ == '__main__':
    app = MangaApp()
    app.run()
