def calculation_power(n):
    # Базовые случаи
    if n == 0 or n == 1:
        return 1  # Датчики версий 0 и 1 делают 1 замер/сек
    return calculation_power(n - 1) + calculation_power(n - 2)


if __name__ == "__main__":
    sensor_version = int(input())
    print(calculation_power(sensor_version))
