import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <input_file>")
        return

    input_file = sys.argv[1]
    output_file = 'employees.tsv'

    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        f_out.write("Name\tSurname\tE-mail\n")
        for line in f_in:
            email = line.strip()
            if not email:
                continue
            try:
                local_part, domain = email.split('@', 1)
                if domain != 'corp.com':
                    continue
                name_part = local_part.split('.', 1)
                if len(name_part) != 2:
                    continue
                name, surname = name_part
                name = name.capitalize()
                surname = surname.capitalize()
                f_out.write(f"{name}\t{surname}\t{email}\n")
            except ValueError:
                continue

if __name__ == "__main__":
    main()