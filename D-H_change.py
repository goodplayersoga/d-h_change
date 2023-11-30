# 模拟Diffie-Hellman密钥交换

def mod_exp(base, exp, modulus):
    # 计算 (base ^ exp) % modulus
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp = exp // 2
        base = (base * base) % modulus
    return result


def diffie_hellman_key_exchange(p, g, private_key):
    # 计算公钥
    public_key = mod_exp(g, private_key, p)
    return public_key


def calculate_shared_secret(public_key, private_key, p):
    # 计算共享密钥
    shared_secret = mod_exp(public_key, private_key, p)
    return shared_secret


# 选择参数
p = 113  # 大素数
g = 3   # 生成元

# Alice 选择私钥
private_key_alice = 6
# Bob 选择私钥
private_key_bob = 15

# Alice 计算公钥
public_key_alice = diffie_hellman_key_exchange(p, g, private_key_alice)
print("alice的公钥：", public_key_alice)
# Bob 计算公钥
public_key_bob = diffie_hellman_key_exchange(p, g, private_key_bob)
print("bob的密钥：", public_key_bob)
# 交换公钥
# Alice 收到Bob的公钥
# Bob 收到Alice的公钥

# 计算共享密钥
shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, p)
shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, p)
print("共享密钥：", shared_secret_alice)
# 验证共享密钥的一致性
if shared_secret_alice == shared_secret_bob:
    print("Diffie-Hellman密钥交换成功，共享密钥一致:", shared_secret_alice)
else:
    print("Diffie-Hellman密钥交换失败")

