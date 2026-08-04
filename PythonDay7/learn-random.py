import random

print("RANDOM EMOJI")
print("========================")

emoji_list = ["🌱", "🌾", "🌽", "🥕", "🍅", "🥔", "🚜", "🐄", "🐓"]

while True:
    selected_emoji = random.choice(emoji_list)
    print("Emoji yang terpilih:", selected_emoji)
    input("Press enter to continue...")