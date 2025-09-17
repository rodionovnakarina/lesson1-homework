import pytest
from api_projects import ProjectsApi

BASE_URL = "https://ru.yougile.com/api-v2"

# 👉 вставь сюда свой реальный токен (из /api-v2/auth/keys)
TOKEN = "HcU3KtgQGJ5t2Cbj1rFpdxQPLkfJhNlR3O0a86sFM2WBGGe5epfJ4JP9YXKuf8ce"

@pytest.fixture
def api():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    return ProjectsApi(BASE_URL, headers)
