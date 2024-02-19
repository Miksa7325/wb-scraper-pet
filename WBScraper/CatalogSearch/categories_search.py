import json
import requests


def get_categories():

    categories_dict = {}
    url_prefix = "https://www.wildberries.by/catalog?category="

    params = {
        'lang': 'ru',
        'locale': 'by',
        'location': 'by',
    }
    response = requests.get('https://catalog.wb.ru/menu/v10/api', params=params)

    for items in response.json().get('data'):
        if items.get('nodes'):
            nodes_dict = {}
            for nodes in items.get('nodes'):
                if nodes.get('childrenOnly'):
                    children = {}
                    for ch in nodes.get('nodes'):
                        children[ch.get('name')] = f"{url_prefix}{ch.get('id')}"
                else:
                    children = f"{url_prefix}{nodes.get('id')}"
                nodes_dict[nodes.get('name')] = children
            categories_dict[items.get('name')] = nodes_dict

    return categories_dict


def write_json_categories(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        json_text = json.dumps(data, indent=4, ensure_ascii=False)
        f.writelines(json_text)


