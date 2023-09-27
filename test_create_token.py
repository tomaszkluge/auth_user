from datetime import timedelta
from main import create_access_token

# Przykładowe dane użytkownika
user_data = {"sub": "example_user"}

# Tworzenie tokena dostępowego z wygaśnięciem za 30 minut
access_token = create_access_token(user_data, expires_delta=timedelta(minutes=30))

print("Generated Access Token:")
print(access_token)
