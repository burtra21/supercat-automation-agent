# health_monitor.py
'''System health monitoring for SuperCat GTM'''

import psutil
import os
from datetime import datetime, timedelta
from database.connection import db
import logging

logger = logging.getLogger(__name__)

class HealthMonitor:
    '''Monitor system health and performance'''
    
    def __init__(self):
        self.checks = {
            'database': False,
            'disk_space': False,
            'memory': False,
            'recent_activity': False,
            'error_rate': False
        }
    
    def check_database(self):
        '''Check database connectivity'''
        try:
            result = db.client.table('companies').select('count').execute()
            self.checks['database'] = True
            return True, "Database connected"
        except Exception as e:
            self.checks['database'] = False
            return False, f"Database error: {e}"
    
    def check_disk_space(self):
        '''Check available disk space'''
        disk = psutil.disk_usage('/')
        free_gb = disk.free / (1024**3)
        
        if free_gb > 1:
            self.checks['disk_space'] = True
            return True, f"Disk space OK ({free_gb:.1f} GB free)"
        else:
            self.checks['disk_space'] = False
            return False, f"Low disk space ({free_gb:.1f} GB free)"
    
    def check_memory(self):
        '''Check memory usage'''
        memory = psutil.virtual_memory()
        
        if memory.percent < 90:
            self.checks['memory'] = True
            return True, f"Memory OK ({memory.percent:.1f}% used)"
        else:
            self.checks['memory'] = False
            return False, f"High memory usage ({memory.percent:.1f}%)"
    
    def check_recent_activity(self):
        '''Check for recent system activity'''
        try:
            # Check for companies analyzed in last 24 hours
            cutoff = (datetime.now() - timedelta(hours=24)).isoformat()
            
            result = db.client.table('companies').select('count').gte(
                'last_website_scan', cutoff
            ).execute()
            
            if result.data:
                self.checks['recent_activity'] = True
                return True, "Recent activity detected"
            else:
                self.checks['recent_activity'] = False
                return False, "No activity in last 24 hours"
        except:
            self.checks['recent_activity'] = False
            return False, "Could not check activity"
    
    def check_error_logs(self):
        '''Check error rate in logs'''
        try:
            log_file = 'logs/daily_automation.log'
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    lines = f.readlines()[-100:]  # Last 100 lines
                
                errors = sum(1 for line in lines if 'ERROR' in line)
                
                if errors < 10:
                    self.checks['error_rate'] = True
                    return True, f"Error rate OK ({errors} errors in last 100 lines)"
                else:
                    self.checks['error_rate'] = False
                    return False, f"High error rate ({errors} errors)"
            else:
                self.checks['error_rate'] = True
                return True, "No error log found"
        except:
            self.checks['error_rate'] = False
            return False, "Could not check error logs"
    
    def run_all_checks(self):
        '''Run all health checks'''
        
        print("\n" + "=" * 60)
        print("🏥 SYSTEM HEALTH CHECK")
        print(f"Time: {datetime.now()}")
        print("=" * 60)
        
        # Run each check
        checks_to_run = [
            ('Database', self.check_database),
            ('Disk Space', self.check_disk_space),
            ('Memory', self.check_memory),
            ('Recent Activity', self.check_recent_activity),
            ('Error Rate', self.check_error_logs)
        ]
        
        all_healthy = True
        
        for name, check_func in checks_to_run:
            success, message = check_func()
            
            if success:
                print(f"✅ {name}: {message}")
            else:
                print(f"❌ {name}: {message}")
                all_healthy = False
        
        print("=" * 60)
        
        if all_healthy:
            print("✅ SYSTEM HEALTHY")
        else:
            print("⚠️  ISSUES DETECTED - Review above")
        
        print("=" * 60)
        
        return all_healthy

if __name__ == "__main__":
    monitor = HealthMonitor()
    monitor.run_all_checks()
