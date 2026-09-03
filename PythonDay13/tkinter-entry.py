import customtkinter as ctk

app = ctk.CTk()
app.title("Welcome App")
app.geometry("350x400")
app.resizable(False, False)

ctk.set_appearance_mode("light")

def submit_name():
    user_name = entry_name.get()

    if user_name.strip() != "":
        lbl_welcome.configure(text=f"Welcome, {user_name}! 👋")
        lbl_message.configure(text="Have a nice day! ✨")
    else:
        lbl_welcome.configure(text="Please enter your name!")
        lbl_message.configure(text="")

ctk.CTkLabel(
    app,
    text="✨📱✨",
    font=("Segoe UI Rounded", 48)
).pack(pady=(40, 10))

ctk.CTkLabel(
    app,
    text="Please enter your name to continue:",
    font=("Segoe UI Rounded", 13),
    text_color="#475569"
).pack(pady=5)

entry_name = ctk.CTkEntry(
    app,
    placeholder_text="Type your name...",
    font=("Segoe UI Rounded", 14),
    width=200,
    height=40,
    corner_radius=10,
    justify="center"
)
entry_name.pack(pady=10)

btn_submit = ctk.CTkButton(
    app,
    text="Submit",
    font=("Segoe UI Rounded", 14, "bold"),
    width=200,
    height=40,
    corner_radius=10,
    command=submit_name
)
btn_submit.pack(pady=10)

lbl_welcome = ctk.CTkLabel(
    app,
    text="",
    font=("Segoe UI Rounded", 18, "bold"),
    text_color="#1E293B"
)
lbl_welcome.pack(pady=(20, 2))

lbl_message = ctk.CTkLabel(
    app,
    text="",
    font=("Segoe UI Rounded", 13, "italic"),
    text_color="#64748B"
)
lbl_message.pack(pady=0)


app.mainloop()