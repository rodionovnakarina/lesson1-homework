import requests

BASE_URL = "https://yougile.com/api-v2"

def get_companies(login, password):
    url = f"{BASE_URL}/auth/companies"
    payload = {"login": login, "password": password}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    # ⚠️ Подставь сюда свой логин и пароль от YouGile
    print(get_companies("YOUR_LOGIN", "YOUR_PASSWORD"))
