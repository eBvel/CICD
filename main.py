import requests


def get_current_weather(city: str) -> str:
    response = requests.get(url=f"https://wttr.in/{city}?format=%t")
    return f"{city}: {response.text}"


if __name__ == "__main__":
    city = "Москва"
    current_weather = get_current_weather(city)
    print(current_weather)
