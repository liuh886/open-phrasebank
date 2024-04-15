import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser(description="Manage Phrasebanks")
    parser.add_argument('--list', action='store_true', help='List all phrasebank files')
    parser.add_argument('--get', type=str, help='Retrieve and download a specific phrasebank file')
    parser.add_argument('--destination', type=str, help='Destination directory for downloaded file', default='.')

    args = parser.parse_args()

    if args.list:
        # List all phrasebank files
        print("Available Phrasebank Files:")
        for file in os.listdir('phrasebanks'):
            print(file)

    if args.get:
        # Retrieve and download a specific file
        source_path = os.path.join('phrasebanks', args.get)
        if os.path.exists(source_path):
            destination_path = os.path.join(args.destination, args.get)
            shutil.copy(source_path, destination_path)
            print(f"{args.get} has been downloaded to {args.destination}")
        else:
            print("File does not exist.")

if __name__ == '__main__':
    main()
