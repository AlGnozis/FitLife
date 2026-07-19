# Проект FitLife - MVP версия 1.0

# Константа: приветственное сообщение (PEP 8)
WELCOME_MESSAGE = (
    "Добро пожаловать в фитнес-бот FitLife — "
    "ваш персональный ассистент по здоровью. "
    "\nОн поможет вам рассчитать индекс массы тела "
    "(ИМТ) и норму потребления воды."
)

# Константы для расчётов
WATER_PER_KG = 30  # рекомендуемый объём воды — 30 мл на 1 кг массы тела
WATER_IN_LITERS = 1000  # количество миллилитров в одном литре
SEPARATOR = "=" * 50  # разделитель для красивого вывода

print("Привет!")
print(WELCOME_MESSAGE)
print(SEPARATOR)


# 1. Знакомство с пользователем

# Сохраняем имя пользователя (строка)
# Обработка ввода имени
user_name = input("Как вас зовут? ").strip()
if not user_name:
    user_name = "Аноним"
    print(f"! Имя не указано. Будем называть вас: {user_name}.")

# Сохраняем возраст пользователя и преобразуем в целое число (int)
# ввод с валидацией
while True:
    try:
        age_input = input("Сколько вам полных лет? ")
        user_age = int(age_input)
        if user_age <= 0:
            print(
                "! Возраст должен быть положительным числом "
                "(например, 18, 30)."
            )
            continue
        break
    except ValueError:
        print(f"! Ошибка: '{age_input}' — введите целое число (например, 25).")


# 2. Сбор данных для расчётов

# Ввод веса и преобразование в число с плавающей точкой (float)
# ввод с валидацией
while True:
    try:
        weight_input = input(
            "Введите ваш вес в килограммах (например, 70.5): "
        )
        user_weight = float(weight_input.replace(",", "."))  # заменяем запятую
        if user_weight <= 0:
            print("! Вес должен быть положительным числом.")
            continue
        break
    except ValueError:
        print(
            f"! Ошибка: '{weight_input}' — введите число "
            "(например, 65.5, с точкой)."
        )

# Ввод роста и преобразование в число с плавающей точкой (float)
# ввод с валидацией
while True:
    try:
        height_input = input("Введите ваш рост в метрах (например, 1.75): ")
        user_height = float(height_input.replace(",", "."))  # заменяем запятую
        if user_height <= 0:
            print("! Рост должен быть положительным числом.")
            continue
        if user_height > 3.0:
            print(
                "! Слишком большой рост! Проверьте, не ввели ли вы "
                "сантиметры вместо метров."
            )
            continue
        if user_height < 0.5:
            print("! Слишком маленький рост. Пожалуйста, уточните.")
            continue
        break
    except ValueError:
        print(
            f"! Ошибка: '{height_input}' — введите число "
            "(например, 1.75, а не 175)."
        )


# 3. Логика расчетов

# Формула ИМТ: масса тела (кг) ÷ (рост в метрах)²
bmi = user_weight / (user_height ** 2)

# Расчёт рекомендуемого объёма воды
water_ml = user_weight * WATER_PER_KG   # вес (кг) × 30 мл
water_l = water_ml / WATER_IN_LITERS    # перевод в литры


# 4. Вывод красивого результата
print(
    f"{SEPARATOR}\n"
    f"ВАШИ РЕЗУЛЬТАТЫ\n"
    f"{SEPARATOR}\n"
    f"Имя: {user_name}\n"
    f"Возраст: {user_age} лет\n"
    f"Ваш Индекс Массы Тела: {bmi:.1f}\n"
    f"Рекомендуемая норма воды: {water_ml:.0f} мл ({water_l:.1f} л в день)\n"
    f"{SEPARATOR}\n"
    f"\nРасчёт окончен. Берегите здоровье!"
)
