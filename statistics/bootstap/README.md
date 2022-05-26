Описание функций в `bootstrap_CI.py`:
  - **bootstrap_samples(data, n_samples)**: data - выборкa, на основе которой нужно сгенерировать новые выборки, n_samples - сколько нужно сгенерировать выборок.
     Функция генерирует n == len(data) случайных чисел из отрезка [0 : len(data)], создает выборку на основе полученных индексов, и повторяет это n_samples раз.
     
  - **confidence_interval(stats, alpha)**: stats - статистики, расчитанные на выборках полученных методом Бутстрэп, alpha - уровень значимости. Функция расчитывает перцентили: alpha/2(нижняя граница) и 1 - alpha/2(верхняя граница) и возвращает их как границы интервала.


Пример использования находится в файле [`example.ipynb`](https://github.com/simonyelisey/academic/blob/main/statistics/bootstap/example.ipynb)
