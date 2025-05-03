import customtkinter as ctk
import random

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# Основне вікно
root = ctk.CTk()
root.title("God help")
root.geometry("800x600")

# список.жартів
funny_text = [
    "Why did the computer get cold? It forgot to close its Windows!",
    "I'm not lazy, I'm just on energy-saving mode.",
    "404: Joke not found.",
    "Did you try turning it off and on again?",
    "Wi-Fi went down for five minutes, so I had to talk to my family. They seem like nice people."
]

# список.картинок
art = [
    r"""
    (\_/)
    ( •_•)
    />🍪
    """,
    r"""
    ──────▄▀▄─────▄▀▄
    ─────▄█░░▀▀▀▀▀░░█▄
    ─▄▄──█░░░░░░░░░░░█──▄▄
    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
    """,
    r"""
    ︵‿︵‿୨♡୧‿︵‿︵
    (｡♥‿♥｡)
    """,
    r"""
    （＾・ω・＾）
    """,
    r"""
    (づ｡◕‿‿◕｡)づ
    """
]

def change_theme(choice):
    ctk.set_appearance_mode(choice)

theme_f = ctk.CTkFrame(root)
theme_f.pack(side="top", fill="x", pady=5)

themes = ["Light", "Dark", "System"]
for theme in themes:
    btn = ctk.CTkButton(theme_f, text=theme, command=lambda t=theme: change_theme(t))
    btn.pack(side="left", padx=5, pady=5)

# Список кольорів фону
background_colors = [
    "#FFDEE9", "#B5FFFC", "#D5FFD0", "#FFD6A5", "#FFF6BD", "#E0BBE4"
]

# Створюємо Tabview
notebook = ctk.CTkTabview(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Лічильник вкладок
tab_counter = 0

# Функція анімації друкування
def typewr_effec(label, full_text, index=0):
    if index <= len(full_text):
        label.configure(text=full_text[:index])
        label.after(50, typewr_effec, label, full_text, index + 1)

# Функція створення нової вкладки
def create_tabs():
    global tab_counter
    tab_counter += 1

    tab_id = f"Tab {tab_counter}"
    notebook.add(tab_id)
    tab = notebook.tab(tab_id)

    content_frame = ctk.CTkFrame(tab)
    content_frame.pack(pady=20, padx=20, expand=True, fill="both")

    random_bg = random.choice(background_colors)
    content_frame.configure(fg_color=random_bg)

    # Випадково art або жарт
    if random.choice([True, False]):
        text = random.choice(funny_text)
    else:
        text = random.choice(art)
    ###############
    label = ctk.CTkLabel(content_frame, text="", font=("Consolas", 18), justify="center", wraplength=700)
    label.pack(expand=True)

    typewr_effec(label, text)

add_tab_button = ctk.CTkButton(root, text="New Tab", command=create_tabs)
add_tab_button.pack(pady=10)

create_tabs()

root.mainloop()