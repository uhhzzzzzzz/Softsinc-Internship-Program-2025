import argparse
from function import calculate, organize_files, generate_password

def main():
    parser = argparse.ArgumentParser(description="CLI Toolkit")
    subparsers = parser.add_subparsers(dest='command')
    
    # Calculater Command
    calc_parser = subparsers.add_parser('calc')
    calc_parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'])
    calc_parser.add_argument('numbers', nargs='+', help="Numbers to operate on")
    
   #File Organizer command
    file_parser = subparsers.add_parser('organize')
    file_parser.add_argument('directory', help="Directory to organize")
    file_parser.add_argument('--extensions', nargs='+', default=['.txt', '.csv'])
    
   #Password Generator command
    pass_parser = subparsers.add_parser('generate-password')
    pass_parser.add_argument('--length', type=int, default=12)
    pass_parser.add_argument('--no-special', action='store_false', dest='special')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'calc':
            result = calculate(args.operation, args.numbers)
            print(f"Result: {result}")
            
        elif args.command == 'organize':
            message = organize_files(args.directory, args.extensions)
            print(message)
            
        elif args.command == 'generate-password':
            password = generate_password(args.length, args.special)
            print(f"Generated Password: {password}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()