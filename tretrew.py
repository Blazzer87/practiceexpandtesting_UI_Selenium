from datetime import datetime

# Исходная строка даты
date_str = '04121987'

# Преобразование строки в объект datetime
date_object = datetime.strptime(date_str, '%d%m%Y').strftime('%Y-%m-%d')


print(date_object)


