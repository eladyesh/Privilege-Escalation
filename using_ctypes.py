import ctypes
import sys

def elevate():
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        return True  # already elevated
    else:
        params = " ".join([sys.executable] + sys.argv)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        return False  # elevated successfully

def write_protected_file():
    with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as f:
        f.write("127.0.0.1 example.com\n")

if __name__ == '__main__':
    elevated = elevate()
    if elevated:
        print("Running as administrator")
        write_protected_file()
    else:
        print("Elevating privileges...")
