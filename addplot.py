import os
import sys

def main():
    args = sys.argv[1:]    
    if args:
        print("Received arguments:", args)
    else:
        sys.exit(1)

    # Check if the script is being run from the correct directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if not current_dir.endswith('scripts'):
        print("Please run this script from the 'scripts' directory.")
        sys.exit(1)

    # Add the parent directory to the system path
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    sys.path.append(parent_dir)

    print(parent_dir)

if __name__ == "__main__":
    main()
