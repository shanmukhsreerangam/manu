# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 5
        print("adding successfull")

if __name__ == '__main__':
        TestAdd()