from app.core.security import hash_password

fake_users_db = {
    "admin": {
        "username": "admin",
        "password": hash_password("admin123")
    }
}