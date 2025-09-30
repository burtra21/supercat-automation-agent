#!/usr/bin/env python3
import os
import sys

def main():
    print("\n🚀 SuperCat GTM Automation")
    print("=" * 40)
    print("1. Run simple test")
    print("2. Test pain detection")
    print("3. Process CSV prospects")
    print("4. Check database connection")
    print("5. Exit")
    print("=" * 40)
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        os.system("python simple_test.py")
    elif choice == "2":
        os.system("python test_pain_detection.py")
    elif choice == "3":
        csv_file = input("Enter CSV filename: ")
        os.system(f"python upload_prospects.py {csv_file}")
    elif choice == "4":
        os.system('python -c "from database.connection import db; print(\"✅ Database connected!\")"')
    elif choice == "5":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
