from restaurant import get_raw_html_from_url, parse_html_to_days, get_string_days_from_tag, get_menu_from_days

def get_menu_from_sps():
    html = get_raw_html_from_url("https://spsbj.edupage.org/menu/")
    days = parse_html_to_days(html, "span", {"class": "skgdli-menu_ListItem_2-menu_DFText_4"})
    days = get_string_days_from_tag(days)

    return get_menu_from_days(days)