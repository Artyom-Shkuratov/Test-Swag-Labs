# Test-Swag-Labs

Автотесты для сайта [Swag Labs](https://www.saucedemo.com/)  
Проект написан на **Python + Pytest + Selenium** с использованием и поддержкой **Allure Report**.

---

## Функционал
- Проверка успешного логина зарегистрированного пользователя  
- Проверка выхода (logout) пользователя  
- Рандомный выбор пользователя для входа  
- Поддержка Allure-отчётов  

## 🚀 Установка и запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Artyom-Shkuratov/Test-Swag-Labs.git
cd Test-Swag-Labs
```
### 2. Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate   # для Mac/Linux
venv\Scripts\activate      # для Windows

### 3. Установить зависимости
pip install -r requirements.txt


### Обычный запуск:
pytest tests/

### Запуск с Allure-отчётом:
pytest --alluredir=allure-results

### Формирование отчёта:
allure serve allure-results

 ### Стек
	•	Python 3.10+
	•	Pytest
	•	Selenium
	•	Allure-pytest
	
