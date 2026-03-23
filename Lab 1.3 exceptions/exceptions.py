import math

def exceptionTest(lyst):

    try:

        listRoot(lyst)

        displayList(lyst) # intentional error, don't correct

        print(lyst)

    except TypeError:
        print("ERROR: Cannot square root a non-numeric value.")

    except ValueError:
        print("ERROR: Cannot square root a negative number.")

    except:
        print("ERROR: Something went wrong.")

def listRoot(lyst):
    """Replaces elements in a list with their square root"""

    for i in range(len(lyst)):
        lyst[i] = math.sqrt(lyst[i])

def main():

    lyst = [1, 2, 3]
    exceptionTest(lyst)

# The entry point for program execution
if __name__ == "__main__":
    main()
     
    
        
