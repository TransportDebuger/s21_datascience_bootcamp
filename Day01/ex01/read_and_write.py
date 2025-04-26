def parse_line(line):
    fields = []
    current_field = []
    in_quotes = False
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            if in_quotes:
                if i + 1 < len(line) and line[i + 1] == '"':
                    current_field.append('"')
                    i += 1
                else:
                    in_quotes = False
            else:
                in_quotes = True
            i += 1
        elif c == ',' and not in_quotes:
            fields.append(''.join(current_field))
            current_field = []
            i += 1
        else:
            current_field.append(c)
            i += 1
    fields.append(''.join(current_field))
    return fields

def main():
    with open('ds.csv', 'r') as infile, open('ds.tsv', 'w') as outfile:
        for line in infile:
            stripped_line = line.rstrip('\n')
            fields = parse_line(stripped_line)
            tsv_line = '\t'.join(fields) + '\n'
            outfile.write(tsv_line)

if __name__ == '__main__':
    main()