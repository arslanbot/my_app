cat > ~/my_app/main.py << 'EOF'
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Для 32-бит устанавливаем размер окна
Window.size = (360, 640)

class MyApp(App):
    def build(self):
        # Основной контейнер
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок
        label = Label(text='Моё приложение на 32-бит', font_size=24, size_hint=(1, 0.2))
        layout.add_widget(label)
        
        # Кнопка
        button = Button(text='Нажми меня', size_hint=(1, 0.2))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)
        
        # Поле ввода
        self.text_input = TextInput(text='', hint_text='Введите текст...', size_hint=(1, 0.15))
        layout.add_widget(self.text_input)
        
        # Кнопка вывода
        show_btn = Button(text='Показать текст', size_hint=(1, 0.15))
        show_btn.bind(on_press=self.show_text)
        layout.add_widget(show_btn)
        
        # Метка для вывода
        self.output_label = Label(text='', size_hint=(1, 0.3), color=(0.2, 0.8, 0.2, 1))
        layout.add_widget(self.output_label)
        
        return layout
    
    def on_button_press(self, instance):
        instance.text = 'Нажато!'
    
    def show_text(self, instance):
        text = self.text_input.text
        if text:
            self.output_label.text = f'Вы ввели: {text}'
        else:
            self.output_label.text = 'Поле пустое'

if __name__ == '__main__':
    MyApp().run()
EOF
