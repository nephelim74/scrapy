import re


def parse_salary_re(salary_list):
    # Создаем словарь для хранения результатов
    salary_dic = {
        'from': None,
        'up to': None,
        'valuts': None,
        'description': None
    }

    # Объединяем список в строку
    salary_string = ''.join(salary_list)

    # Используем регулярные выражения для поиска значений
    from_match = re.search(r'от\s+([\d\s\xa0]+)', salary_string)
    up_to_match = re.search(r'до\s+([\d\s\xa0]+)', salary_string)
    valuts_match = re.search(r'(\₽)', salary_string)

    # Извлекаем и преобразуем значения
    if from_match:
        salary_dic['from'] = from_match.group(1).replace(' ', '').replace('\xa0', '')
    if up_to_match:
        salary_dic['up to'] = up_to_match.group(1).replace(' ', '').replace('\xa0', '')
    if valuts_match:
        salary_dic['valuts'] = valuts_match.group(1)

    # Извлекаем описание: все остальное, что не является цифрами или валютой
    description_match = re.sub(r'от\s+[\d\s\xa0]+|до\s+[\d\s\xa0]+|(\₽)', '', salary_string)
    salary_dic['description'] = description_match.strip()

    return salary_dic

