import shutil
import time
from datetime import datetime

DISK_PATH = "/"
INTERVAL_SEC = 2
WARN_THRESHOLD = 80
CRIT_THRESHOLD = 90

def fmt_gb(n_bytes):
    return f"{n_bytes / (1024 ** 3):.2f} GB"

def main():
    print(f"{'时间':<20} | {'总容量':<10} | {'已用':<10} | {'剩余':<10} | {'使用率'}")
    print("-" * 75)
    
    try:
        while True:
            total, used, free = shutil.disk_usage(DISK_PATH)
            pct = used / total * 100
            ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            status = ""
            if pct >= CRIT_THRESHOLD: status = " [!!! 严重 !!!]"
            elif pct >= WARN_THRESHOLD: status = " [! 警告 !]"
            
            print(f"{ts:<20} | {fmt_gb(total):<10} | {fmt_gb(used):<10} | {fmt_gb(free):<10} | {pct:.2f}%{status}")
            
            time.sleep(INTERVAL_SEC)
    except KeyboardInterrupt:
        print("\n监控已停止。")

if __name__ == "__main__":
    main()