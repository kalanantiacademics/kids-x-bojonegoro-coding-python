import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.title("Image Viewer")
app.geometry("350x450")

ctk.set_appearance_mode("light")

image_path = Image.open("plant.jpg")

title_image =ctk.CTkImage(
    light_image=image_path,
    dark_image=image_path,
    size=(200, 200)
)

ctk.CTkLabel(
    app,
    text="Plant Dictionary",
    font=("Arial", 24, "bold"),
    text_color="#1B5E20"
).pack(pady=(30, 15))

ctk.CTkLabel(
    app,
    image=title_image,
    text=""
).pack(pady=10)

ctk.CTkLabel(
    app,
    text="Complete Guide & Flora Directory", 
    font=("Arial", 14, "italic"),
    text_color="#555555"
).pack(pady=10)

app.mainloop()