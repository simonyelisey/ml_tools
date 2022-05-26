import numpy as np


def bootstrap_samples(data: np.array, n_samples: int):
    """
    Функция генерирует новые выборки методом Bootstrap

    :param data: np.array - генеральная выборка, на основе котораой генерируются выборки
    :param n_samples: int-  количество генерируемых выборок
    :return: np.array размера n_samples x len(data) - каждая строчка сгенерированная выборка
    """
    # генерация случайных индексов от 0 до len(data)
    idxs = np.random.randint(0, len(data), size=(n_samples, len(data)))
    # создание выборкок на основе сгенерированных индексов
    bootstrapsamples = data[idxs]

    return bootstrapsamples


def confidence_interval(stats_list: np.array, alpha: float):
    """
    Функция создает доверительный интервал статистик, полученных из сгенерированных выборок методом Bootstrap

    :param stats_list: np.array - список статистик, посчитанных на всех выборках
    :param alpha: float - уровень значимости
    :return: list с нижней и верхней границей доверительного интервала
    """
    low_boundary = np.percentile(stats_list, 100 * alpha / 2)
    high_boundary = np.percentile(stats_list, 100 * (1 - alpha / 2))

    return [low_boundary, high_boundary]
  
