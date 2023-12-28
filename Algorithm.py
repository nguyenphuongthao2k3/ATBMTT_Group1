import hashlib
import random
from math import gcd


def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def modinv(a, m):
    """Tìm nghịch đảo modulo."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_large_prime():
    """Sinh một số nguyên tố lớn."""
    while True:
        num = random.randint(10**14, 10**15)
        if is_prime(num):
            return num


def generate_keypair():
    """Sinh khoá công khai và bí mật."""
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    # Chọn số e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Sử dụng thuật toán Euclide mở rộng để tính số d
    d = modinv(e, phi)

    return ((n, e), (n, d))

def hash_message(message):
    """Hàm băm văn bản sử dụng SHA-1 và chỉ lấy 16 ký tự đầu tiên."""
    hashed_message = hashlib.sha256(str(message).encode()).hexdigest()
    return int(hashed_message[:8], 16)



def sign(message, private_key):
    """Ký bản tin."""
    n, d = private_key
    hashed_message = hash_message(message)
    print('1',hashed_message)
    signature = pow(hashed_message, d, n)
    return signature


def verify(message, signature, public_key):
    """Kiểm thử chữ ký."""
    n, e = public_key

    decrypted_signature = pow(signature, e, n)
    print(f'd1 {decrypted_signature}')
    # Hash the original message for comparison
    hashed_message = hash_message(message)
    print(f's2: {hashed_message}')
    return decrypted_signature == hashed_message


def decrypt(ciphertext, public_key):
    """Giải mã bản tin."""
    n, e = public_key
    plaintext = pow(ciphertext, e, n)
    return plaintext

# Example usage
if __name__ == "__main__":
    # Bước 1: Sinh khoá
    public_key, private_key = generate_keypair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Bước 2: Ký và kiểm thử chữ ký
   # message = random.randint(1, public_key[0] - 1)
    message = 123
    print("Original Message:", message)

    signature = sign(message, private_key)
    print("Signature:", signature)
    verification_result = verify(message, signature, public_key)
    print("Verification Result:", verification_result)

    # Bước 3: Giải mã khi xác thực thành công
    if verification_result:
        decrypted_message = decrypt(signature, public_key)
        print("Decrypted Message:", decrypted_message)
