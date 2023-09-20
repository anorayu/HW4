import numpy as np

# Создание двумерного массива
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Вывод элемента, расположенного в правом верхнем углу массива
top_right_element = array[0, -1]
print("Элемент в правом верхнем углу массива:", top_right_element)

# Вывод элемента, расположенного в левом нижнем углу массива
bottom_left_element = array[-1, 0]
print("Элемент в левом нижнем углу массива:", bottom_left_element)