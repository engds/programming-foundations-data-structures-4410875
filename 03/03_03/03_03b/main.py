user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

user_preferences["language"]="Kiswahili"
user_preferences["fav_dish"]="omena"

for key, value in user_preferences.items():
  print(f"{key} | {value}")
