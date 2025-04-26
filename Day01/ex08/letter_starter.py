import sys

def main():
    if len(sys.argv) != 2:
        return

    target_email = sys.argv[1].strip()

    try:
        with open('employees.tsv', 'r') as f:
            next(f)  # Skip header
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 3:
                    continue
                email = parts[2]
                if email == target_email:
                    name = parts[0]
                    print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                    return
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()