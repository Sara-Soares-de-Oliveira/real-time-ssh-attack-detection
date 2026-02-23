from __future__ import annotations

from monitor.log_watcher import tail_lines

if __name__ == "__main__":
    path="/var/log/auth.log" #mover para config
    for line in tail_lines(path):
        print(line)