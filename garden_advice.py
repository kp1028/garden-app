# Hardcoded values for the season and plant type

season = input("What is the season: ")  # Added input for user interaction
plant_type = input("What is the plant type: ") # Added input for user interaction

# Variable to hold gardening advice
advice = ""

# Based on the user interaction and what they inputted
# it will provide advice to their respective answers on the season.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Based on the user interaction and what they inputted,
# it will provide advice to their respective answers on the plant type.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
