csv_file = 'data.csv'
num_steps = 3
report_template = '''Report
We have made {observations} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {tail_percent:.2f}% and {head_percent:.2f}%, respectively. Our forecast is that in the next {num_steps} observations we will have: {next_tails} tail and {next_heads} heads.'''