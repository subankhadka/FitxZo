# Function definition
def traffic_decision(signal_colour):
    signal_colour = signal_colour.lower()  # handle case sensitivity
    
    if signal_colour == "red":
        return "Stop! Stay behind the crosswalk."
    
    elif signal_colour == "yellow":
        return "Slow down! Prepare to stop safely."
    
    elif signal_colour == "green":
        return "Go! The path is clear."
    
    else:
        return "Warning: Invalid signal colour detected."

# Taking dynamic input from user
user_input = input("What colour is the traffic signal right now? ")

# Passing input to function and printing result
decision = traffic_decision(user_input)
print(decision)
