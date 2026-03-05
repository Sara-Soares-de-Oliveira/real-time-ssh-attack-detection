from __future__ import annotations

from monitor.log_watcher import tail_lines
from detector.failed_login_detector import FailedLoginDetector


def main():
    path="/var/log/auth.log" #mover para config
    
    detector = FailedLoginDetector()
    
    for line in tail_lines(path):
       blocked_ip = detector.process_line(line)
       
       if blocked_ip:
        
           info = detector.get_attack_info(blocked_ip) 
           users = ", ".join(info['users'])
           attempts = info['attempts_window']
           total_attempts = info['total_attempts']
           
           print(
                f"Failed login attempt detected: IP:{blocked_ip} exceeded threshold |"
                f"Users targeted:{users} | "
                f"Attempts={attempts} |"
                f"Total Attempts={total_attempts}" 
                )



if __name__ == "__main__":
    main()
    
    