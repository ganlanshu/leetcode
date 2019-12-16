# coding=utf-8
import sys


def gcd(a, b):
    """
    欧几里得算法求最大公约数 gcd(a, b) = gcd(b, a%b), gcd(a, 0) = a
    :param a:
    :param b:
    :return:
    """
    while b != 0:
        a, b = b, a % b

    return a


def gcd_ext(a, b):
    if b == 0:
        return 1, 0
    k = a // b
    remainder = a % b
    x1, y1 = gcd_ext(b, remainder)
    x, y = y1, x1 - k*y1
    return x, y


def get_decrypt_key(encrypt_key):
    p = 23333
    q = 10007
    phi = (p-1) * (q-1)
    decrypted_key, _ = gcd_ext(encrypt_key, phi)
    if decrypted_key < 0:
        decrypted_key = decrypted_key % phi
    return decrypted_key


def power_mod(base, pow_num, mod_num):
    ans = 1
    base = base % mod_num
    while pow_num > 0:
        if pow_num % 2 == 1:
            ans = (ans * base) % mod_num
        pow_num = pow_num // 2
        base = (base*base) % mod_num
    return ans


def main(encrypt_key_message):
    line = encrypt_key_message.strip().split(' ')
    encrypt_key, encrypted_message = int(line[0]), int(line[1])
    decrypted_key = get_decrypt_key(encrypt_key)
    p = 23333
    q = 10007
    n = p * q
    original_message = power_mod(encrypted_message, decrypted_key, n)
    return original_message


if __name__ == '__main__':
    encrypt_key_message = input()
    output = main(encrypt_key_message)
    print(output)
