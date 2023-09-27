from main import get_password_hash

# Przykładowe hasło użytkownika
password = "example_password"

# Generowanie skrótu (hash) hasła
hashed_password = get_password_hash(password)

print("Generated Hashed Password:")
print(hashed_password)
