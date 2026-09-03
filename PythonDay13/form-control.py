import customtkinter as ctk

app = ctk.CTk()
app.title("Plant Data Management - Desktop App")
app.geometry("620x340")
app.resizable(False, False)

ctk.set_appearance_mode("light")

radio_var = ctk.StringVar(value="Indoor")

def submit_data():
    name = entry_name.get()
    category = combo_category.get()
    area_type = radio_var.get()
    needs_watering = "Yes" if check_water.get() == 1 else "No"

    if name.strip() != "":
        lbl_result.configure(
            text=f"🌱 Name: {name}\n\n"
                 f"📦 Category: {category}\n\n"
                 f"🏡 Area Type: {area_type}\n\n"
                 f"💧 Daily Watering: {needs_watering}"
        )
    else:
        lbl_result.configure(text="⚠️ Please enter a plant name first!")

ctk.CTkLabel(
    app,
    text="📝 Plant Data Management System",
    font=("Segoe UI Rounded", 18, "bold"),
    text_color="#15803D"
).pack(pady=(15, 10))

main_container = ctk.CTkFrame(app, fg_color="transparent")
main_container.pack(fill="both", expand=True, padx=20, pady=5)

main_container.grid_columnconfigure((0, 1), weight=1, uniform="column_group")
main_container.grid_rowconfigure(0, weight=1)

left_frame = ctk.CTkFrame(main_container, fg_color="transparent")
left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

entry_name = ctk.CTkEntry(
    left_frame,
    placeholder_text="Plant Name...",
    font=("Segoe UI Rounded", 12),
    height=35,
    corner_radius=8,
    border_color="#86EFAC",
    fg_color="#F0FDF4"
)
entry_name.pack(fill="x", pady=6)

combo_category = ctk.CTkComboBox(
    left_frame,
    values=["Ornamental", "Fruit", "Vegetable", "Medicinal"],
    font=("Segoe UI Rounded", 12),
    dropdown_font=("Segoe UI Rounded", 12),
    height=35,
    corner_radius=8,
    fg_color="#DCFCE7",
    text_color="#166534",
    button_color="#86EFAC",
    button_hover_color="#4ADE80",
    border_color="#86EFAC"
)
combo_category.set("Select Category")
combo_category.pack(fill="x", pady=6)

frame_radio = ctk.CTkFrame(left_frame, fg_color="transparent")
frame_radio.pack(fill="x", pady=6)

radio1 = ctk.CTkRadioButton(
    frame_radio,
    text="Indoor",
    value="Indoor",
    font=("Segoe UI Rounded", 12),
    text_color="#374151",
    fg_color="#22C55E",
    hover_color="#16A34A",
    variable=radio_var,
)
radio1.pack(side="left", padx=(0, 15))

radio2 = ctk.CTkRadioButton(
    frame_radio,
    text="Outdoor",
    value="Outdoor",
    font=("Segoe UI Rounded", 12),
    text_color="#374151",
    fg_color="#22C55E",
    hover_color="#16A34A",
    variable=radio_var,
)
radio2.pack(side="left")

check_water = ctk.CTkCheckBox(
    left_frame, 
    text="Daily Watering Needed 💧",
    font=("Segoe UI Rounded", 12),
    text_color="#374151",
    fg_color="#22C55E",
    hover_color="#16A34A"
)
check_water.pack(anchor="w", pady=8)

btn_submit = ctk.CTkButton(
    left_frame, 
    text="Save Data ✨", 
    font=("Segoe UI Rounded", 13, "bold"),
    height=38,
    corner_radius=8,
    fg_color="#22C55E",
    text_color="#FFFFFF",
    hover_color="#16A34A",
    command=submit_data
)
btn_submit.pack(fill="x", pady=(10, 0))

right_frame = ctk.CTkFrame(
    main_container, 
    fg_color="#F0FDF4", 
    corner_radius=10,
    border_width=1,
    border_color="#DCFCE7"
)
right_frame.grid(row=0, column=1, sticky="nsew", pady=(0, 20))

ctk.CTkLabel(
    right_frame,
    text="📋 Data Preview",
    font=("Segoe UI Rounded", 13, "bold"),
    text_color="#166534"
).pack(anchor="w", padx=15, pady=(15, 5))

lbl_result = ctk.CTkLabel(
    right_frame, 
    text="Fill out the form on the left\nand click Save Data.", 
    font=("Segoe UI Rounded", 12),
    text_color="#374151",
    justify="left"
)
lbl_result.pack(anchor="w", padx=15, pady=10)


app.mainloop()