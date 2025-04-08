import datetime
import random

# Your motivational quotes
quotes = [
    "Keep pushing forward 🚀",
    "You're doing great! 🌟",
    "Consistency is the key 🔑",
    "One step at a time 👣",
    "Every line of code counts 💻",
    "Believe in the process 🙌",
    "Progress > Perfection ✅"
]

# Get today's date and a random quote
today = datetime.datetime.now().strftime("%Y-%m-%d")
quote = random.choice(quotes)
entry = f"{today} - {quote}"

# Read old log entries
try:
    with open("streak.log", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

# Add today's entry and keep only the last 7
lines.append(entry + "\n")
lines = lines[-7:]

# Write back to the log
with open("streak.log", "w") as f:
    f.writelines(lines)
