import random
import pyjokes
import randfacts
import requests

OPENWEATHER_API_KEY = '8bf651322efd1ca15c312b9a7d2e1f8e'

# a dictionary that stores the keywords and different types of responses
responses = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greetings"],
        "outputs": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to see you. What's on your mind?"
        ]
    },
    "weather": {
        "keywords": ["weather", "forecast"],
        "outputs": [
            "Sure, I can check the weather for you. What city would you like to know about?",
            "I'd be happy to provide a weather update. Which city are you interested in?",
            "Let me fetch the weather for you. What's the name of the city?"
        ]
    },
    "help": {
        "keywords": ["help", "support", "what can you do", "features"],
        "outputs": [
            "I'm here to assist you! Here's what I can do:\n"
            "1. Greet you and engage in general conversation\n"
            "2. Provide weather information for any city, type 'weather' to search for a city\n"
            "3. Tell you jokes, type 'joke'\n"
            "4. Share interesting facts, type 'fact'\n"
            "5. Offer help and list my features, type 'help'"
        ]
    },
    "joke": {
        "keywords": ["joke", "funny"],
        "outputs": [
            "Sure, here's a joke for you: ",
            "Get ready to laugh! Here's a joke: ",
            "I've got a good one for you: "
        ]
    },
    "fact": {
        "keywords": ["fact", "trivia"],
        "outputs": [
            "Here's an interesting fact for you: ",
            "Did you know? ",
            "Fun fact time! "
        ]
    }
}

# a funcation that utelizes the OpenWeather api to get the weather by a city name
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    try:
        api_response = requests.get(url)
        json_data = api_response.json() 
        
        return f"The current temperature in {city} is {json_data['main']['temp']}°C with {json_data['weather'][0]['description']}."
    
    except:
        return f"Sorry, I couldn't fetch the weather information for {city}. Try to ask for weather again."

# function that matches user input with appropriate response
def find_response(user_input):
    user_input = user_input.lower() 

    for response_type, data in responses.items():
        if any(keyword in user_input for keyword in data["keywords"]):

            if response_type == "joke":
                return random.choice(data["outputs"]) + pyjokes.get_joke()
            
            elif response_type == "fact":
                return random.choice(data["outputs"]) + randfacts.get_fact()
            
            else:
                return random.choice(data["outputs"])
    
    return "I'm sorry, I don't understand that. Can you try rephrasing or ask for help?"

print("YahliBot: Hello! I'm YahliBot, the best chatbot. Type 'bye' to exit or 'help' to see what I can do.")
weather_query = False
while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    if weather_query:
        response = get_weather(user_input)
        weather_query = False 

    else:
        response = find_response(user_input)
        if "weather" in user_input.lower():
            weather_query = True
    
    print("YahliBot:", response)
