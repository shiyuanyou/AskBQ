from cryptography.fernet import Fernet
import json
import argparse

# 1. 生成或加载加密密钥
def generate_key():
    """生成一个新的加密密钥"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """加载加密密钥"""
    return open("secret.key", "rb").read()

# 2. 加密API密钥
def encrypt_api_key(api_key, key):
    """使用密钥加密API密钥"""
    f = Fernet(key)
    encrypted_key = f.encrypt(api_key.encode())
    return encrypted_key

# 3. 解密API密钥
def decrypt_api_key(encrypted_key, key):
    """使用密钥解密API密钥"""
    f = Fernet(key)
    decrypted_key = f.decrypt(encrypted_key)
    return decrypted_key.decode()

# 4. 保存加密后的API密钥到配置文件
def save_encrypted_key_to_config(encrypted_key):
    config = {"encrypted_api_key": encrypted_key.decode()}
    with open("config.json", "w") as config_file:
        json.dump(config, config_file)

# 5. 从配置文件中读取加密的API密钥
def load_encrypted_key_from_config():
    try:    
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
        return config["encrypted_api_key"].encode()
    except Exception as e:
        print(f"Error loading encrypted key from config: {e}")
        raise e

def init_key():
    """初始化加密密钥"""
    try:
        key = load_key()
        print("已加载现有密钥")
    except FileNotFoundError:
        generate_key()
        key = load_key()
        print("已生成新密钥")
    return key

def main():
    parser = argparse.ArgumentParser(description='API密钥加密工具')
    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # 初始化密钥的命令
    init_parser = subparsers.add_parser('init', help='初始化或重新生成加密密钥')

    # 加密API密钥的命令
    encrypt_parser = subparsers.add_parser('encrypt', help='加密API密钥')
    encrypt_parser.add_argument('api_key', help='要加密的API密钥')

    # 解密API密钥的命令
    decrypt_parser = subparsers.add_parser('decrypt', help='解密API密钥')

    args = parser.parse_args()

    if args.command == 'init':
        init_key()
        print("密钥初始化完成")

    elif args.command == 'encrypt':
        key = init_key()
        encrypted_key = encrypt_api_key(args.api_key, key)
        save_encrypted_key_to_config(encrypted_key)
        print("API密钥已加密并保存到配置文件")

    elif args.command == 'decrypt':
        key = init_key()
        try:
            encrypted_key = load_encrypted_key_from_config()
            decrypted_key = decrypt_api_key(encrypted_key, key)
            print(f"解密后的API密钥: {decrypted_key}")
        except FileNotFoundError:
            print("错误: 未找到配置文件，请先加密API密钥")
        except Exception as e:
            print(f"解密失败: {str(e)}")

    else:
        parser.print_help()

def getKey():
    key = init_key()
    try:
        encrypted_key = load_encrypted_key_from_config()
        ret_key = decrypt_api_key(encrypted_key, key)
        return ret_key
    except Exception as e:
        print(f"没有初始化密钥，请先初始化密钥: {e}")
        print("请先执行: python encrypt.py init")
        print("然后执行: python encrypt.py encrypt 'your-api-key-here'")
        raise e

if __name__ == "__main__":
    main()