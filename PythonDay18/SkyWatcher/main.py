import customtkinter as ctk
import requests

API_KEY = "967f4ebc064e9a796ff53137866b9e87"

def fetch_weather(event=None):
    city = entry_city.get().strip()
    if not city:
        return

    # 1. Ambil koordinat kota
    geo_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    geo_data = requests.get(geo_url).json()
    
    if not geo_data:
        lbl_status.configure(text="❌ Kota tidak ditemukan", text_color="#EF4444")
        return

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]
    name = geo_data[0]["name"]


    # 2. Ambil data cuaca
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=id"
    data = requests.get(weather_url).json()

    print(data)

    # 3. Update Tampilan UI
    lbl_city.configure(text=name.upper())
    lbl_temp.configure(text=f"{data['main']['temp']:.1f}°C")
    lbl_desc.configure(text=data['weather'][0]['description'].title())
    lbl_humidity.configure(text=f"{data['main']['humidity']}%")
    lbl_wind.configure(text=f"{data['wind']['speed']} m/s")
    lbl_status.configure(text="✅ Berhasil!", text_color="#10B981")

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("SkyWatch Weather Monitor")
app.geometry("480x680")
app.configure(fg_color="#F8FAFC")

title = ctk.CTkLabel(
    app,
    text="Sky Watcher",
    font=("Segoe UI", 26, "bold"),
    text_color="#0F172A"
)
title.pack(pady=(28, 4))

subtitle = ctk.CTkLabel(
    app,
    text="Real-time Weather Updates",
    font=("Segoe UI", 12),
    text_color="#64748B"
)
subtitle.pack(pady=(0, 20))

input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=5)

entry_city = ctk.CTkEntry(
    input_frame,
    width=310,
    height=44,
    placeholder_text="Enter city,country (e.g. Jakarta,ID)",
    corner_radius=12,
    border_width=1,
    border_color="#CBD5E1",
    fg_color="#FFFFFF",
    text_color="#0F172A",
    font=("Segoe UI", 13)
)
entry_city.pack(side="left", padx=(0, 8))
entry_city.insert(0, "")

weather_card = ctk.CTkFrame(app, fg_color="#FFFFFF", corner_radius=20, border_width=1, border_color="#E2E8F0")
weather_card.pack(fill="x", padx=35, pady=(20, 15))

lbl_city = ctk.CTkLabel(
    weather_card,
    text="YOUR CITY",
    font=("Segoe UI", 20, "bold"),
    text_color="#1E293B"
)
lbl_city.pack(pady=(20, 4))

lbl_icon = ctk.CTkLabel(weather_card, text="⛅", font=("Segoe UI Emoji", 64))
lbl_icon.pack(pady=0)

lbl_temp = ctk.CTkLabel(
    weather_card,
    text="-- °C",
    font=("Segoe UI", 48, "bold"),
    text_color="#0F172A"
)
lbl_temp.pack(pady=(0, 2))

lbl_desc = ctk.CTkLabel(
    weather_card,
    text="Press SEARCH to load weather",
    font=("Segoe UI", 13),
    text_color="#64748B"
)
lbl_desc.pack(pady=(0, 20))

stats = ctk.CTkFrame(app, fg_color="#F1F5F9", corner_radius=16)
stats.pack(fill="x", padx=35, pady=10)
stats.grid_columnconfigure((0, 1), weight=1)

# Humidity Group
ctk.CTkLabel(
    stats,
    text="💧 HUMIDITY",
    font=("Segoe UI", 11, "bold"),
    text_color="#64748B"
).grid(row=0, column=0, pady=(14, 0))

lbl_humidity = ctk.CTkLabel(
    stats,
    text="--%",
    font=("Segoe UI", 20, "bold"),
    text_color="#0F172A"
)
lbl_humidity.grid(row=1, column=0, pady=(2, 14))

# Wind Group
ctk.CTkLabel(
    stats,
    text="💨 WIND SPEED",
    font=("Segoe UI", 11, "bold"),
    text_color="#64748B"
).grid(row=0, column=1, pady=(14, 0))

lbl_wind = ctk.CTkLabel(
    stats,
    text="-- m/s",
    font=("Segoe UI", 20, "bold"),
    text_color="#0F172A"
)
lbl_wind.grid(row=1, column=1, pady=(2, 14))

lbl_status = ctk.CTkLabel(
    app,
    text="Data provided by OpenWeatherMap",
    font=("Segoe UI", 11),
    text_color="#94A3B8"
)
lbl_status.pack(side="bottom", pady=15)

btn_search = ctk.CTkButton(
    input_frame,
    text="🔍 Search",
    width=90,
    height=44,
    corner_radius=12,
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    font=("Segoe UI", 13, "bold"),
    command=fetch_weather
)
btn_search.pack(side="left")


app.mainloop()


