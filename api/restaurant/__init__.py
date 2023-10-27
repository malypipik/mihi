import requests

from bs4 import BeautifulSoup

def get_raw_html_from_url(url: str) -> str:
    response = requests.get(url).text
    return response.text

def parse_html_to_days(html: str, find_name: str, find_attr: dict) -> dict:
    bs = BeautifulSoup(html, features="lxml")
    return bs.find_all(find_name, find_attr)

def get_string_days_from_tag(tag_list):
    days_string_list = []

    for tag in tag_list:
        days_string_list.append(tag.text)

    return days_string_list

def get_day_from_number(day_id: int) -> str:
    week_days = {
        0: "Monday", 
        1: "Tuesday", 
        2: "Wednesday", 
        3: "Thursday", 
        4: "Friday", 
        5: "Saturday", 
        6: "Sunday"
    }

    return week_days[day_id]

def parse_meals_from_day(day):
    meals = []

    for meal in day.split('\n'):
        if meal == "":
            continue

        meals.append(meal)

    return meals

def get_menu_from_days(days):
    menu_map = {}
    day_id = 0

    for day in days:
        menu_map[get_day_from_number(day_id)] = parse_meals_from_day(day)
        day_id += 1

    return menu_map