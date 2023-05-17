import argparse

parser = argparse.ArgumentParser(description='Sum some numbers')
parser.add_argument('integers', type=int, nargs='+',
                    help='a number to sum up.')
args = parser.parse_args()

print(sum(args.integers))
print(min(args.integers))
print(max(args.integers))






#import sys
#n = (sys.argv)
#print(sum(len(n[1] + n[2])))
#print(min(n[1]+n[2]))
#print(max(n[1]+n[2]))



#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("luku1", help="syota luku 1", type=int)
#parser.add_argument("luku2", help="syota luku 2", type=int)

#args = parser.parse_args()
#print(f'Yhteenlaskettu {args.luku1 + args.luku2}')
#print(f'Pienin summa {len(args.luku1 , args.luku2)}')

#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument("luku", type=int, nargs=3)
#args = parser.parse_args()
#sum = sum(args.values)
#print("Sum: ", sum)

