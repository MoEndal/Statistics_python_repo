import argparse

parser = argparse.ArgumentParser(description='Sum some numbers')
parser.add_argument('integers', type=int, nargs='+',
                    help='a number to sum up.')
args = parser.parse_args()

print(sum(args.integers))
print(min(args.integers))
print(max(args.integers))