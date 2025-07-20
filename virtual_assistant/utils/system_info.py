import psutil

def get_cpu_info():
    return f"CPU usage: {psutil.cpu_percent()}%"

def get_ram_info():
    mem = psutil.virtual_memory()
    return f"RAM: {mem.used // (1024 ** 2)}MB used / {mem.total // (1024 ** 2)}MB total"

def get_disk_info():
    disk = psutil.disk_usage('/')
    return f"Disk: {disk.used // (1024 ** 3)}GB used / {disk.total // (1024 ** 3)}GB total"