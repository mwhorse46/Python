import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv)

if len(sys.argv) > 1:
    print(sys.argv[1])
