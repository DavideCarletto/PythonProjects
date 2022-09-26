import numpy as np

def create_functions():
    # check if a function is a ufunc:

    print(f"Type of add function: {type(np.add)}")
    print(f"Type of concatenate function: {type(np.concatenate)}")

    # Create own ufunc
    def myadd(x, y):
        return x + y

    myadd = np.frompyfunc(myadd, 2, 1) # 2 is the number of inputs, 1 is the number of outputs

    print(f"Array added with the myadd function: {myadd([1, 2, 3, 4], [5, 6, 7, 8])}")

    print(f"Type of myadd function: {type(myadd)}")

def array_simpleAritmetic():

    arr1 = np.array([10, 11, 12, 13, 14, 15])
    arr2 = np.array([20, 21, 22, 23, 24, 25])

    print(f"First array: {arr1}")
    print(f"Second array: {arr2}\n")

    print(f"Addition: {np.add(arr1,arr2)}")
    print(f"Subtraction: {np.subtract(arr1,arr2)}")
    print(f"Multiplication: {np.multiply(arr1,arr2)}")
    print(f"Power: {np.power(arr1,arr2)}")
    print(f"Remainder: {np.mod(arr1,arr2)}")
    print(f"Quotient and Mod: {np.divmod(arr1,arr2)}")
    print(f"Absolute Values: {np.absolute(np.subtract(arr1,arr2))}")

def main():
    #create_functions()
    array_simpleAritmetic()

if __name__ == "__main__":
    # ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
    main()