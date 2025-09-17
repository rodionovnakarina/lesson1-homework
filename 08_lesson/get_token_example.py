import requests

BASE_URL = "https://yougile.com/api-v2"

def get_token(login, password, company_id):
    url = f"{BASE_URL}/auth/keys"
    payload = {
        "login": login,
        "password": password,
        "companyId": company_id
    }
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    # ⚠️ Сюда наставник должен подставить свои данные:
    print(get_token("YOUR_LOGIN", "YOUR_PASSWORD", "YOUR_COMPANY_ID"))
