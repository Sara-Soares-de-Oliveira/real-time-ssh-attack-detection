import re
import time

class FailedLoginDetector:
    
   
    def __init__(self,pattern=None):
        if pattern is None:
            # Padrão para detectar falhas de login (ajuste conforme necessário)
           pattern = r'Failed (?:password|publickey) for (?:invalid user )?(\S+) from (\S+) port \d+ ssh\d+'
        
        self.pattern = re.compile(pattern)
        self.attempts = {} # Dicionário para armazenar tentativas de login por IP
        
        self.threshold = 3  # Número de tentativas antes de bloquear o IP
        self.time_window = 120  # Janela de tempo em segundos (2 minutos)
         
    
    def process_line(self, line: str):
        match = self.pattern.search(line)
    
        timestamp = time.time()
      
        limit = timestamp - self.time_window
        
        if not match:
            return None
          
        user = match.group(1)
                
        ip = match.group(2)
            
        if ip not in self.attempts:
           self.attempts[ip] = {
                "timestamps": [],
                "users": set(),
                "blocked": False, 
                "total_attempts": 0
            }
            
        clear_past_attempts = [t for t in self.attempts[ip]["timestamps"] if t > limit]
            
        self.attempts[ip]["timestamps"] = clear_past_attempts
            
        self.attempts[ip]["timestamps"].append(timestamp)
        self.attempts[ip]["users"].add(user)
        self.attempts[ip]["total_attempts"] += 1
    
            
            
        if len(self.attempts[ip]["timestamps"]) >= self.threshold and not self.attempts[ip]["blocked"]:
            self.attempts[ip]["blocked"] = True
            return  ip
        else: 
            return None
             
    def get_attack_info(self, ip):
        if ip in self.attempts:
            return {
                "users": set(self.attempts[ip]["users"]),
                "attempts_window": len(self.attempts[ip]["timestamps"]),
                "total_attempts": self.attempts[ip]["total_attempts"]
            }
        return None    