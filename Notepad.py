from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.title('My Notepad') # Название окна приложения
root.geometry('700x500+550+300') #  Размера окна приложения. Длина х Ширина х Ось Х х Ось Y
root.iconbitmap('notepad.ico') # Установка иконки приложения, если в той же папке где и файл, то просто название иконки пишем

main_menu = Menu(root)
root.config(menu = main_menu)

def about_program():
    messagebox.showinfo(title = 'About notepad', message = 'Программа Notepad v 0.0.1\n''Ждите обновлений')
    
    
def m_exit():
    answer = messagebox.askokcancel(title = 'Выход', message = 'Закрыть программу?')
    if answer:
        root.destroy()
        
def open_file():
    file_path = filedialog.askopenfilename(title = 'Выбор файла', filetypes = (('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        t.delete('1.0', END) # от первого символа первой стороки до конца
        t.insert('1.0', open(file_path).read())
    
def save_file():
    file_path = filedialog.asksaveasfilename(title = 'Сохранить файл', filetypes = (('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w')
    text = t.get('1.0', END)
    f.write(text)
    f.close()
    
    
def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']
    

#File
file_menu = Menu(main_menu, tearoff = 0)
file_menu.add_command(label = 'Открыть', command = open_file)
file_menu.add_command(label = 'Сохранить', command = save_file)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = m_exit)
main_menu.add_cascade(label = 'Файл', menu = file_menu)


#Theme
theme_menu = Menu(main_menu, tearoff = 0)
theme_menu_sub = Menu(theme_menu, tearoff = 0)
theme_menu_sub.add_command(label = 'Dark', command = lambda: change_theme('light'))
theme_menu_sub.add_command(label = 'Light',command = lambda: change_theme('dark'))
theme_menu.add_cascade(label = 'Темы', menu = theme_menu_sub)
main_menu.add_cascade(label = 'Оформление', menu = theme_menu)

#About
about_menu = Menu(main_menu, tearoff = 0)
about_menu_sub = Menu(about_menu, tearoff = 0)
about_menu_sub.add_command(label = 'О программе', command = about_program)
main_menu.add_cascade(label = 'Справка', menu = about_menu_sub)

# f_menu = Frame(root, bg = '#1F252A', height = 40) место для подменю
# f_menu.pack(fill = X) место для подменю
f_text = Frame(root)
f_text.pack(fill = BOTH, expand = 1)

theme_colors = {
    'dark': {
        'text_bg': '#fff', 'text_fg': '#000', 'cursor': '#EDA756', 'select_bg': '#4E5A65'
        },
    'light': {
        'text_bg': '#343D46', 'text_fg': '#fff', 'cursor': '#8000FF', 'select_bg': '#777'
        }
}
t = Text(f_text, bg = theme_colors['dark']['text_bg'], fg = theme_colors['dark']['text_fg'], padx = 10, pady = 10, wrap = WORD, insertbackground = theme_colors['dark']['cursor'],
         selectbackground = theme_colors['dark']['select_bg'], spacing3 = 10, width = 30, font = ('Courier New', 11)) # font настройка шрифта, width/height высота - ширина кнопки
t.pack(fill = BOTH, expand = 1, side = LEFT) 

scroll = Scrollbar(f_text, command = t.yview)
scroll.pack(fill = Y, side = LEFT)
t.config(yscrollcommand = scroll.set)



root.mainloop()