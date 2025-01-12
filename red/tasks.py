import requests

def fetch_weather_data(station_id):
    try:
        print(f"Pobieranie danych dla stacji {station_id}...")

        response = requests.get(f"http://127.0.0.1:8000/weather/{station_id}")

        if response.status_code == 200:
            data = response.json()
            temp = float(data["temperature"])
            
            if temp > 30:
                print(f"wysoka temperatura {temp}'C na stacji {station_id}")
            return data

        else:
            print(f"Błąd API, kod odpowiedzi: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        print(f"Nie można polaczyc sie z API dla staci {station_id}")
        return None
    except Exception as e:
        print(f"Blad dla stacji {station_id} {e}")
        return None

if __name__ == "__main__":
    fetch_weather_data("STACJA_TESTOWA")