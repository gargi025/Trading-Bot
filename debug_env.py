from bot.config import Config

print("API Key:", Config.API_KEY)
print("Secret Exists:", Config.API_SECRET is not None)
print("Base URL:", Config.BASE_URL)
