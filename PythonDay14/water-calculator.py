import customtkinter as ctk

app = ctk.CTk()
app.title("Crop Water Calculator")
app.geometry("380x600")
app.resizable(False, False)

ctk.set_appearance_mode("light")

season_var = ctk.StringVar(value="Dry")

def calculate_water():
    area_text = entry_area.get()
    crop_type = combo_crop.get()
    season = season_var.get()
    is_drip = check_drip.get()

    try:
        area = float(area_text)
        if area <= 0:
            lbl_result.configure(text="⚠️ Area must be greater than 0!", text_color="#EF4444")
            return
    except ValueError:
        lbl_result.configure(text="⚠️ Enter a valid number for Area!", text_color="#EF4444")
        return

    base_water_rate = 5.0
    if crop_type == "Rice 🌾":
        base_water_rate = 8.0
    elif crop_type == "Corn 🌽":
        base_water_rate = 6.0
    elif crop_type == "Vegetables 🥬":
        base_water_rate = 4.0

    season_multiplier = 0
    if season == "Dry":
        season_multiplier = 1.2
    else:
        season_multiplier = 0.8

    total_water = area * base_water_rate * season_multiplier

    if is_drip == 1:
        total_water *= 0.8

    lbl_result.configure(
        text_color="#1E293B",
        text=f"🌾 Area: {area:,.0f} m²\n\n"
             f"🌱 Crop: {crop_type}\n\n"
             f"☀️ Season: {season}\n\n"
             f"💧 Water Needed:\n"
             f"   👉 {total_water:,.1f} Liters/day"
    )

ctk.CTkLabel(
    app,
    text="💧 Crop Water Calculator",
    font=("Segoe UI Rounded", 20, "bold"),
    text_color="#0284C7"
).pack(pady=(20, 12))

form_frame = ctk.CTkFrame(
    app,
    fg_color="#F0F9FF",
    corner_radius=14,
    border_width=1,
    border_color="#BAE6FD"
)
form_frame.pack(fill="x", padx=20, pady=5)

entry_area = ctk.CTkEntry(
    form_frame,
    placeholder_text="Enter Field Area (m²)...",
    placeholder_text_color="#64748B",
    height=40,
    corner_radius=8,
    border_color="#7DD3FC",
    fg_color="#FFFFFF",
    text_color="#0F172A"
)
entry_area.pack(fill="x", padx=15, pady=(15, 8))

combo_crop = ctk.CTkComboBox(
    form_frame,
    values=["Vegetables 🥬", "Corn 🌽", "Rice 🌾"],
    height=40,
    corner_radius=8,
    fg_color="#FFFFFF",
    text_color="#0369A1",
    dropdown_fg_color="#FFFFFF",
    dropdown_text_color="#0F172A",
    button_color="#7DD3FC",
    button_hover_color="#38BDF8",
    border_color="#7DD3FC"
)
combo_crop.set("Vegetables 🥬")
combo_crop.pack(fill="x", padx=15, pady=8)

frame_radio = ctk.CTkFrame(form_frame, fg_color="transparent")
frame_radio.pack(fill="x", padx=15, pady=8)

radio_dry = ctk.CTkRadioButton(
    frame_radio,
    text="Dry",
    value="Dry",
    fg_color="#EAB308",
    hover_color="#CA8A04",
    text_color="#1E293B",
    variable = season_var
)
radio_dry.pack(side="left", padx=(0, 20))

radio_rainy = ctk.CTkRadioButton(
    frame_radio, text="Rainy",
    value="Rainy",
    fg_color="#EAB308",
    hover_color="#CA8A04",
    text_color="#1E293B",
    variable = season_var
)
radio_rainy.pack(side="left")

check_drip = ctk.CTkCheckBox(
    form_frame,
    text="Use Drip Irrigation (-20% water)",
    fg_color="#EAB308",
    hover_color="#CA8A04",
    text_color="#1E293B"
)
check_drip.pack(anchor="w", padx=15, pady=(8, 15))

btn_calc = ctk.CTkButton(
    app,
    text="Calculate Water Needs 📊",
    font=("Segoe UI Rounded", 14, "bold"),
    height=45,
    corner_radius=10,
    fg_color="#FEF08A",
    text_color="#713F12",
    hover_color="#FDE047",
    command=calculate_water
)
btn_calc.pack(fill="x", padx=20, pady=12)

result_frame = ctk.CTkFrame(
    app,
    fg_color="#FEFCE8",
    corner_radius=14,
    border_width=1,
    border_color="#FEF08A"
)
result_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

ctk.CTkLabel(
    result_frame,
    text="📋 Result Preview",
    font=("Segoe UI Rounded", 13, "bold"),
    text_color="#854D0E"
).pack(anchor="w", padx=15, pady=(12, 5))

lbl_result = ctk.CTkLabel(
    result_frame,
    text="Fill in the field size and options,\nthen tap Calculate.",
    font=("Segoe UI Rounded", 12),
    text_color="#64748B",
    justify="left"
)
lbl_result.pack(anchor="w", padx=15, pady=5)


app.mainloop()