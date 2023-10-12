"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int: 
    """Угадываем число, используя метод половинного деления
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """    
 
    count=0
    
    start = 1  # устанавливаем нижнию границу интервала
    end = 101  # устанавливаем верхнюю границу интервала
    
    while True:
        count += 1
        predict_number = int((start + end)/2) # вычисляем середину отрезка и округляем до целого
        
        if predict_number == number:
            break
        
        elif predict_number > number:
            end = predict_number  # меняем верхнюю границу интервала
            
        elif predict_number < number:
            start = predict_number  # меняем нижнюю границу интервала          
          
    return count
    
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """   
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:        
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))    
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    #RUN
    score_game(random_predict)
    