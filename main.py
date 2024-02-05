# Реализация кодера кода Хэмминга
def hamming_encoder(data):
    # Вычисляем количество битов коррекции
    r = 0
    while 2**r <= len(data) + r + 1:
        r += 1

    # Вставляем позиции для битов коррекции
    encoded_data = []
    j = 0
    k = 0
    for i in range(1, len(data) + r + 1):
        if i == 2**k:
            encoded_data.insert(i-1, 0)
            k += 1
        else:
            encoded_data.insert(i-1, int(data[j]))
            j += 1

    # Вычисляем значения битов коррекции
    for i in range(r):
        index = 2**i - 1
        j = index
        xor = 0
        while j < len(encoded_data):
            xor ^= encoded_data[j]
            j = j + 2**(i + 1)
        encoded_data[index] = xor

    return encoded_data


# Реализация декодера кода Хэмминга
def hamming_decoder(received_data):
    # Вычисляем количество битов коррекции
    r = 0
    while 2**r < len(received_data):
        r += 1

    # Вычисляем значения битов коррекции
    error_pos = 0
    for i in range(r):
        index = 2**i - 1
        j = index
        xor = 0
        while j < len(received_data):
            xor ^= received_data[j]
            j = j + 2**(i + 1)
        if xor != 0:
            error_pos += index + 1

    # Если обнаружена ошибка, исправляем её
    if error_pos != 0:
        received_data[error_pos-1] = 1 - received_data[error_pos-1]

    # Удаляем биты коррекции
    decoded_data = []
    for i in range(len(received_data)):
        if i != 0 and i & (i + 1) != 0:
            decoded_data.append(received_data[i])

    return decoded_data

if __name__ == "main":
    text = input('Введите то, что надо закодировать')
    hamming_encoder(text)