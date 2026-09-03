import customtkinter as ctk

app = ctk.CTk()
app.title("Cookie Clicker")
app.geometry("350x450")
app.resizable(False, False)

ctk.set_appearance_mode("light")

count = 0

def count_click():
    global count
    count += 1
    lbl_score.configure(text=str(count))

def count_restart():
    global count
    count = 0
    lbl_score.configure(text=str(count))

ctk.CTkLabel(
    app,
    text="🍪 Cookie Bakery 🍪",
    font=("Comic Sans MS", 16, "bold"),
    text_color="#B08968"
).pack(pady=(40, 5))

lbl_score = ctk.CTkLabel(
    app,
    text="0",
    font=("Comic Sans MS", 64, "bold"),
    text_color="#7F5539"
)
lbl_score.pack(pady=5)

ctk.CTkLabel(
    app,
    text="cookies baked",
    font=("Comic Sans MS", 12, "italic"),
    text_color="#9C6644"
).pack(pady=(0, 20))

btn_cookie = ctk.CTkButton(
    app,
    text="BAKE! 🍪",
    font=("Comic Sans MS", 20, "bold"),
    width=180,
    height=60,
    corner_radius=30,
    fg_color="#E6CCB2",
    text_color="#7F5539",
    hover_color="#DDB892",
    border_width=2,
    border_color="#B08968",
    command=count_click
)
btn_cookie.pack(pady=20)

btn_restart = ctk.CTkButton(
    app,
    text="RESTART",
    font=("Comic Sans MS", 20, "bold"),
    width=180,
    height=60,
    corner_radius=30,
    fg_color="#E6CCB2",
    text_color="#7F5539",
    hover_color="#DDB892",
    border_width=2,
    border_color="#B08968",
    command=count_restart
)
btn_restart.pack(pady=20)

app.mainloop()