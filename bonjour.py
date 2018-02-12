
"""
The worl's most awesome bonjour monde module
"""
import sys

def bonjour(name='Monde'):
    """
    Return a greeting for a given name.
    """
    return 'Bonjour, {}'.format(name)


def main():
    """
    Reads input from args passed into the script and prints the output to stout.
    """
    args=sys.argv[1:]
    name = ' '.join(args)
    if name:
        print(bonjour(name))
    else:
        print(bonjour())

if __name__ == '__main__':
    main()