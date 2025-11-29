import numpy as np


def bit_reverse(bin):
    """
    Recebe uma string binária, inverte a ordem dos bits e retorna
    o valor numérico (inteiro) correspondente ao novo binário.
    """

    # Inverte a ordem dos bits na string
    bin_reverse = bin[::-1]

    # Converte a string binária invertida de volta para um inteiro
    # return int(bin_reverse, 2)
    return bin_reverse


def t_fft(cpx, n, sign):
    return


def f_fft(cpx, n, sign):
    return


# teste reverse
a = input("Digite um binário: ")
rev = bit_reverse(a)
print("Binário invertido: ", rev)