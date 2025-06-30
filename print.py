from decouple import config
print("DB_USER:", config('DB_USER'))
print("DB_PASSWORD:", config('DB_PASSWORD'))
