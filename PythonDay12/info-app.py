import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.title("AgriInfo App")
app.geometry("400x550")
app.resizable(False, False)

ctk.set_appearance_mode("light")

img_farmer = ctk.CTkImage(
    light_image=Image.open("farmer.png"),
    dark_image=Image.open("farmer.png"),
    size=(100, 100)
)

img_crop = ctk.CTkImage(
    light_image=Image.open("crop.png"),
    dark_image=Image.open("crop.png"),
    size=(100, 100)
)

img_water = ctk.CTkImage(
    light_image=Image.open("water.png"),
    dark_image=Image.open("water.png"),
    size=(100, 100)
)

def show_frame(target_frame):
    frame_home.pack_forget()
    frame_farmers.pack_forget()
    frame_crops.pack_forget()
    frame_water.pack_forget()

    target_frame.pack(fill="both", expand=True)

frame_home = ctk.CTkFrame(app, fg_color="transparent")
frame_home.pack(pady=10, padx=10, fill="both", expand=True)

ctk.CTkLabel(
    frame_home,
    text="🌾 Agriculture Hub",
    font=("Segoe UI Rounded", 22, "bold"),
    text_color="#22C55E"
).pack(pady=(30, 20))

frame_grid = ctk.CTkFrame(frame_home, fg_color="transparent")
frame_grid.pack(pady=10, padx=20)

frame_grid.grid_columnconfigure((0, 1), weight=1)

btn_farmers = ctk.CTkButton(
    frame_grid, 
    image=img_farmer,
    text="Farmers", 
    compound="top",
    font=("Segoe UI Rounded", 12, "bold"),
    width=130, height=130, corner_radius=15,
    fg_color="#DCFCE7", text_color="#15803D", hover_color="#BBF7D0",
    command=lambda: show_frame(frame_farmers)
)
btn_farmers.grid(row=0, column=0, padx=10, pady=10)

btn_crops = ctk.CTkButton(
    frame_grid, 
    image=img_crop,
    text="Crop Yield", 
    compound="top",
    font=("Segoe UI Rounded", 12, "bold"),
    width=130, height=130, corner_radius=15,
    fg_color="#FEF3C7", text_color="#B45309", hover_color="#FDE68A",
    command=lambda: show_frame(frame_crops)
)
btn_crops.grid(row=0, column=1, padx=10, pady=10)

btn_water = ctk.CTkButton(
    frame_grid, 
    image=img_water,
    text="Water Stress", 
    compound="top",
    font=("Segoe UI Rounded", 12, "bold"),
    width=130, height=130, corner_radius=15,
    fg_color="#E0F2FE", text_color="#0369A1", hover_color="#BAE6FD",
    command=lambda: show_frame(frame_water)
)
btn_water.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

frame_farmers = ctk.CTkFrame(app, fg_color="transparent")

ctk.CTkLabel(
    frame_farmers,
    text="👨‍🌾 Farmers Directory",
    font=("Segoe UI Rounded", 20, "bold"),
    text_color="#15803D"
).pack(pady=(40, 15))

ctk.CTkLabel(
    frame_farmers,
    text="Empowering local farming communities with modern agricultural tools and market access to ensure sustainable food production.",
    font=("Segoe UI Rounded", 13),
    wraplength=300,
    text_color="#374151"
).pack(pady=20)

ctk.CTkButton(
    frame_farmers,
    text="← Back to Home",
    font=("Segoe UI Rounded", 12, "bold"),
    fg_color="#334155", hover_color="#1E293B",
    command=lambda: show_frame(frame_home)
).pack(side="bottom", pady=30)

frame_crops = ctk.CTkFrame(app, fg_color="transparent")

ctk.CTkLabel(
    frame_crops, 
    text="🌽 Crop Yield Data", 
    font=("Segoe UI Rounded", 20, "bold"), 
    text_color="#B45309"
).pack(pady=(40, 15))

ctk.CTkLabel(
    frame_crops, 
    text="Tracking seasonal harvest performance and soil nutrient levels to optimize crop rotation and maximize total harvest efficiency.",
    font=("Segoe UI Rounded", 13), 
    wraplength=300, 
    text_color="#374151"
).pack(pady=20)

ctk.CTkButton(
    frame_crops, 
    text="← Back to Home", 
    font=("Segoe UI Rounded", 12, "bold"),
    fg_color="#334155", hover_color="#1E293B",
    command=lambda: show_frame(frame_home)
).pack(side="bottom", pady=30)

frame_water = ctk.CTkFrame(app, fg_color="transparent")

ctk.CTkLabel(
    frame_water, 
    text="💧 Water Stress Level", 
    font=("Segoe UI Rounded", 20, "bold"), 
    text_color="#0369A1"
).pack(pady=(40, 15))

ctk.CTkLabel(
    frame_water, 
    text="Monitoring soil moisture levels and rainfall indices to prevent drought stress and improve smart irrigation scheduling.",
    font=("Segoe UI Rounded", 13), 
    wraplength=300, 
    text_color="#374151"
).pack(pady=20)

ctk.CTkButton(
    frame_water, 
    text="← Back to Home", 
    font=("Segoe UI Rounded", 12, "bold"),
    fg_color="#334155", hover_color="#1E293B",
    command=lambda: show_frame(frame_home)
).pack(side="bottom", pady=30)


show_frame(frame_home)

app.mainloop()