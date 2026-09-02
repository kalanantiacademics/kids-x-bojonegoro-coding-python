import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.title("Plant Dictionary")
app.geometry("400x650")

ctk.set_appearance_mode("light")

plant_images = [
    Image.open("aloe-vera.jpg"),
    Image.open("lavender.jpg"),
    Image.open("fiddle-leaf-fig.jpg"),
    Image.open("snake-plant.jpg"),
    Image.open("golden-pothos.jpg"),
    Image.open("monstera-deliciosa.jpg"),
]

img_aloevera = ctk.CTkImage(light_image=plant_images[0], dark_image=plant_images[0], size=(100, 100))
img_lavender = ctk.CTkImage(light_image=plant_images[1], dark_image=plant_images[1], size=(100, 100))
img_fiddleleaf = ctk.CTkImage(light_image=plant_images[2], dark_image=plant_images[2], size=(100, 100))
img_snakeplant = ctk.CTkImage(light_image=plant_images[3], dark_image=plant_images[3], size=(100, 100))
img_goldenpothos = ctk.CTkImage(light_image=plant_images[4], dark_image=plant_images[4], size=(100, 100))
img_montseradeliciosa = ctk.CTkImage(light_image=plant_images[5], dark_image=plant_images[5], size=(100, 100))

frame_header = ctk.CTkFrame(
    app,
    fg_color="#E8F5E9",
    corner_radius=2
)
frame_header.pack(fill="x")

ctk.CTkLabel(
    frame_header,
    text="Plant Dictionary",
    font=("Arial", 22, "bold"),
    text_color="#1B5E20"
).pack(side="top")

ctk.CTkLabel(
    frame_header,
    text="Complete Guide & Flora Directory",
    font=("Arial", 12, "italic"),
    text_color="#64748B"
).pack(side="top")

frame_body = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
frame_body.pack(fill="x", pady=10)

frame_body.grid_columnconfigure((0, 1), weight=1)
frame_body.grid_rowconfigure((0, 1), weight=1)

ctk.CTkLabel(
    frame_body,
    image=img_aloevera,
    text=""
).grid(row=0, column=0, padx=5, pady=10)

ctk.CTkLabel(
    frame_body,
    image=img_lavender,
    text=""
).grid(row=0, column=1, padx=5, pady=10)

ctk.CTkLabel(
    frame_body,
    image=img_fiddleleaf,
    text=""
).grid(row=1, column=0, padx=5, pady=10)

ctk.CTkLabel(
    frame_body,
    image=img_snakeplant,
    text=""
).grid(row=1, column=1, padx=5, pady=10)

ctk.CTkLabel(
    frame_body,
    image=img_goldenpothos,
    text=""
).grid(row=2, column=0, padx=5, pady=10)

ctk.CTkLabel(
    frame_body,
    image=img_montseradeliciosa,
    text=""
).grid(row=2, column=1, padx=5, pady=10)

frame_footer = ctk.CTkFrame(app, fg_color="#F1F5F9", corner_radius=0)
frame_footer.pack(fill="x", side="bottom")

ctk.CTkLabel(
    frame_footer,
    text="Version 1.0.0",
    font=("Arial", 12, "italic"),
    text_color="#64748B"
).pack(pady=10)


app.mainloop()