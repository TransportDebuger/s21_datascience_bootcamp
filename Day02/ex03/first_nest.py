import sys

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):
        try:
            with open(self.file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
        except IOError as e:
            raise IOError(f"Could not read file: {e}")

        if has_header:
            if len(lines) < 2:
                raise ValueError("Not enough lines: expected at least a header and one data line.")
            header = lines[0].split(',')
            if len(header) != 2 or not header[0] or not header[1]:
                raise ValueError("Header must be two comma-separated strings.")
            data_lines = lines[1:]
        else:
            if not lines:
                raise ValueError("No data lines found.")
            data_lines = lines

        data = []
        for line in data_lines:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f"Line '{line}' must contain exactly two comma-separated values.")
            try:
                a, b = int(parts[0]), int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid values in line '{line}': must be integers.")
            if a not in (0, 1) or b not in (0, 1):
                raise ValueError(f"Values in line '{line}' must be 0 or 1.")
            if a == b:
                raise ValueError(f"Values in line '{line}' must be different.")
            data.append([a, b])
        return data

    class Calculations:
        @staticmethod
        def counts(data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return (heads, tails)
        
        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            return (heads / total * 100, tails / total * 100)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python first_nest.py <filepath>")
        sys.exit(1)
    try:
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)
        heads, tails = Research.Calculations.counts(data)
        print(f"{heads} {tails}")
        head_percent, tail_percent = Research.Calculations.fractions(heads, tails)
        print(f"{head_percent} {tail_percent}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)