# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(2,3) == 65
        assert Add(5,5) == 10
        print("adding successfull")

if __name__ == '__main__':
        TestAdd()