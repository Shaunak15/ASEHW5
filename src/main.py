import sys
import getopt
import inputs  # import inputs module
from tests import *  # import test functions from tests module

def run_tests():
    """Execute all test functions in the test suite and print the results."""
    print("Executing tests...\n")

    passCount = 0
    failCount = 0
    test_suite = [test_nums, test_sym, test_the, test_half, test_csv, test_data, test_clone, test_cliffs, test_tree, test_dist, test_sway, test_bins]
    
    for test in test_suite:
        try:
            test()
            passCount += 1
        except AssertionError:
            failCount += 1
    
    print(f"\nPassing: {passCount}\nFailing: {failCount}")

# Define command line options
options = "hg"
long_options = []

def main():
    """Parse command line arguments and execute the appropriate function."""
    argumentList = sys.argv[1:]
    
    try:    
        # Parsing arguments
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # Checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ('-h', ''):
                # Print help string and exit
                print(inputs.help_string)
                return
            elif currentArgument in ("-g", ''):
                # Run test suite
                run_tests()
                return
                
    except getopt.error as err:
        # Print error message and exit
        print(str(err))

if __name__ == "__main__":
    main()
