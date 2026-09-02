import customtkinter as ctk

app = ctk.CTk()
app.title("Plant Dictionary")
app.geometry("350x450")

ctk.set_appearance_mode("light")

ctk.CTkLabel(
    app,
    text="📖🌿",
    font=("Arial", 70)
).pack(pady=(80, 10))

ctk.CTkLabel(
    app,
    text="Plant Dictionary",
    font=("Arial", 26, "bold"),
    text_color="#1B5E20"
).pack(pady=5)

ctk.CTkLabel(
    app, 
    text="Complete Guide & Flora Directory", 
    font=("Arial", 12, "italic"),
    text_color="#555555"
).pack(pady=5)

ctk.CTkLabel(
    app, 
    text="Loading app...", 
    font=("Arial", 11),
    text_color="#888888"
).pack(side="bottom", pady=30)

app.mainloop()