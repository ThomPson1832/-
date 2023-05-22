from cryptography.fernet import Fernet

# 生成一个随机的密钥
key = Fernet.generate_key()

# 创建一个加密对象
cipher_suite = Fernet(key)

# 要加密的数据
message = "Hello, world!".encode()

# 加密数据
cipher_text = cipher_suite.encrypt(message)

print(f"密文：{cipher_text}")

# 解密数据
plain_text = cipher_suite.decrypt(cipher_text)

print(f"明文：{plain_text.decode())")
