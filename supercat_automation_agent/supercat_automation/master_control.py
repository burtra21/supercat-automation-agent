#!/usr/bin/env python3
# master_control.py
'''Master control panel for SuperCat GTM - Enhanced'''

import os
import sys
from datetime import datetime

def main():
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 70)
        print("🚀 SUPERCAT GTM AUTOMATION - MASTER CONTROL v2.0")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        print("\n📋 MAIN OPERATIONS")
        print("  1. Run Full Pipeline (Complete)")
        print("  2. Analyze Companies Only")
        print("  3. Generate Campaigns Only")
        print("  4. Process CSV File")
        
        print("\n🔧 TESTING & MONITORING")
        print("  5. Run Simple Test")
        print("  6. View Performance Dashboard")
        print("  7. System Health Check")
        
        print("\n📊 REPORTS & EXPORTS")
        print("  8. Generate All Reports")
        print("  9. Export Qualified Prospects")
        print("  10. Export Campaign Messages")
        
        print("\n⚙️ ADMINISTRATION")
        print("  11. Start Daily Automation")
        print("  12. View SQL Migrations")
        print("  13. Check Database Status")
        print("  0. Exit")
        
        print("=" * 70)
        choice = input("\nSelect option: ")
        
        if choice == "1":
            print("\n🚀 Running full pipeline...")
            os.system("python full_orchestrator.py full")
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            print("\n🔍 Running analysis only...")
            os.system("python full_orchestrator.py analysis_only")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            print("\n✉️ Generating campaigns...")
            os.system("python full_orchestrator.py campaign_only")
            input("\nPress Enter to continue...")
            
        elif choice == "4":
            csv_file = input("Enter CSV filename (or 'sample' for sample_prospects.csv): ")
            if csv_file == 'sample':
                csv_file = 'sample_prospects.csv'
            if os.path.exists(csv_file):
                os.system(f"python upload_prospects.py {csv_file}")
            else:
                print(f"❌ File not found: {csv_file}")
            input("\nPress Enter to continue...")
            
        elif choice == "5":
            print("\n🧪 Running simple test...")
            os.system("python simple_test.py")
            input("\nPress Enter to continue...")
            
        elif choice == "6":
            print("\n📊 Performance Dashboard")
            os.system("python performance_dashboard.py")
            input("\nPress Enter to continue...")
            
        elif choice == "7":
            print("\n🏥 System Health Check")
            os.system("python health_monitor.py")
            input("\nPress Enter to continue...")
            
        elif choice == "8":
            print("\n📊 Generating all reports...")
            os.system("python reporting.py")
            input("\nPress Enter to continue...")
            
        elif choice == "9":
            print("\n📤 Exporting qualified prospects...")
            os.system('python -c "from reporting import ReportGenerator; r = ReportGenerator(); r.export_qualified_prospects()"')
            input("\nPress Enter to continue...")
            
        elif choice == "10":
            print("\n📤 Exporting campaign messages...")
            os.system('python -c "from reporting import ReportGenerator; r = ReportGenerator(); r.export_campaign_messages()"')
            input("\nPress Enter to continue...")
            
        elif choice == "11":
            print("\n⏰ Starting daily automation...")
            print("This will run continuously. Press Ctrl+C to stop.")
            confirm = input("Start automation? (y/n): ")
            if confirm.lower() == 'y':
                os.system("python automated_daily.py")
            
        elif choice == "12":
            print("\n📋 SQL Migrations")
            print("Copy and run in Supabase SQL editor:")
            print("-" * 40)
            os.system("cat create_tables.sql 2>/dev/null || type create_tables.sql 2>nul")
            input("\nPress Enter to continue...")
            
        elif choice == "13":
            print("\n🔍 Checking database...")
            os.system('python -c "from database.connection import db; print(\'✅ Database connected!\')"')
            input("\nPress Enter to continue...")
            
        elif choice == "0":
            print("\n👋 Goodbye!")
            sys.exit(0)
        
        else:
            print("\n❌ Invalid option")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
