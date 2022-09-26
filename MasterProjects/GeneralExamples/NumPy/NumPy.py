import numpy as np
import matplotlib.pyplot as plt

# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

def create_arrays():
    array = np.array([1, 2, 3, 4, 5])
    list = [1, 2, 3, 4, 5, ]

    print(array * 5)
    print(list * 5)

    print(type(array))
    print(type(list))

    a_0D = np.array(43)
    a_1D = np.array([1,2,3,4,5])
    a_2D = np.array([[1,2],[3,4],[5,6]])
    a_3D = np.array([[[1,2],[3,4],[5,6]],[[1,2],[3,4],[5,6]]])
    a_4D = np.array([[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]],[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]])
    a_5D = np.array([1,2,3,4,5], ndmin = 5)
    a_arange = np.arange(5,50)
    a_zeros = np.zeros((3,2,2))
    a_ones = np.ones((2,2,3))

    print(f"Dim = {a_0D.ndim}:\n{a_0D}")
    print("----------")
    print(f"Dim = {a_1D.ndim}:\n{a_1D[::2]}")
    print("----------")
    print(f"Dim = {a_2D.ndim}:\n{a_2D[0:2,:]}")
    print("----------")
    print(f"Dim = {a_3D.ndim}:\n{a_3D[0:2,0:2,:]}")
    print("----------")
    print(f"Dim = {a_4D.ndim}:\n{a_4D[0:2,0:2,0:2,:]}")
    print("----------")
    print(f"Dim = {a_5D.ndim}:\n{a_5D}")
    print("----------")
    print(f"Dim = {a_arange.ndim}:\n{a_arange[::2]}")
    print("----------")
    print(f"Dim = {a_zeros.ndim}:\n{a_zeros}")
    print("----------")
    print(f"Dim = {a_ones.ndim}:\n{a_ones}")
    print("----------")

def data_type():

    arr_int = np.array([0,1,2,3,4], dtype="i")
    arr_str = np.array([1,2,3,4,5],dtype= "U4")
    arr_int_to_str = arr_int.astype("U4")      #create a copy of the array
    arr_float = np.array([1.1,2.3,3.2])
    arr_bool = arr_int.astype(bool)

    print(f"Array 1: %35s   \t\tData type: %10s"%(arr_int, arr_int.dtype))
    print(f"Array 2: %35s   \t\tData type: %10s"%(arr_str, arr_str.dtype))
    print(f"Array 3: %35s   \t\tData type: %10s"%(arr_int_to_str, arr_int_to_str.dtype))
    print(f"Array 4: %35s   \t\tData type: %10s"%(arr_float.astype("f"), arr_float.dtype))
    print(f"Array 5: %35s   \t\tData type: %10s"%(arr_bool, arr_bool.dtype))

def plot_arrays():
    #a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    #plt.plot(a)
    #---------------------------------------------------------
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    X = np.arange(-5, 5, 0.15)
    Y = np.arange(-5, 5, 0.15)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
    plt.show()


def copy_view_array():
    arr = np.array([1,2,3,4,5])
    arr_cpy = arr.copy() #create another array

    arr[0] = 0

    print("%10s Base: %5s"%(arr, arr.base))
    print("%10s Base: %5s"%(arr_cpy, arr_cpy.base))

    arr_view = arr.view() #is the same array

    arr[0] = 20

    print()
    print("%10s Base: %5s" % (arr, arr.base))
    print("%10s Base: %5s" % (arr_view, arr_view.base))


def shape_array():
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

    print(f"Array shape: {arr.shape}")

    arr_reshaped = arr.reshape(4,3)

    print(f"Array reshaped: {arr_reshaped}, Base: {arr_reshaped.base}, so it is a view.")

    arr_reshaped3D = arr.reshape(2,2,-1) #-1 is the unknown dimension, meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
    #the multi among numbers must be the amount of numbers in the non-shaped array

    print()
    print(f"Array reshaped: {arr_reshaped3D}")

    print()
    print(f"Array flattened: {arr_reshaped3D.reshape(-1)}")
    # or arr_reshape3D.flatten()

def iteration_array():
    arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(2,2,3)
    print(f"Array:{arr}")
    print()

    # 1-way: using for loops
    
    print("First iteration:\n ")
    print("[", end=" ")
    for x in arr:
        for y in x:
            for z in y:
                print(z, end = " ")

    print("]")
    print("----------\n")

    # 2-way: using nditer (with different data types)

    print("Second iteration:\n ")
    print("[", end=" ")
    for x in np.nditer(arr[:,:,::2],flags=['buffered'], op_dtypes=['U']):
        print(x, end = " ")
    print("]")
    print("----------\n")

    # 3-way: using enumerate (it stores the index in a tuple)

    print("Third iteration:\n ")
    for index,x in np.ndenumerate(arr):
        print(index, x)
    print("----------\n")

def join_array():
    arr1 = np.array([1,2,3,4,5,6])
    arr2 = np.array([7,8,9,10,11,12])

    arr = np.concatenate((arr1,arr2))

    print(f"First array: {arr1}")
    print(f"Second array: {arr2}")
    print(f"First array concatenated: {arr}\n")

    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[7,8,9],[10,11,12]])

    c = np.concatenate((a,b), axis=1)

    print(f"First array: {a}")
    print(f"Second array: {b}")
    print(f"Array 2D concatenated (by axis being = 1): {c}\n")

    # Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

    d = np.array([1, 2, 3])
    e = np.array([4, 5, 6])

    f = np.stack((d, e), axis=1)

    print(f"First array: {d}")
    print(f"Second array: {e}")
    print(f"Array concatenated by stack (new axis = 1): {f}\n")

    # Stacking along rows: hstack

    g = np.array([1, 2, 3])
    h = np.array([4, 5, 6])

    i = np.hstack((g, h))

    print(f"First array: {g}")
    print(f"Second array: {h}")
    print(f"Array concatenated by hstack: {i}\n")

    # Stacking along columns: vstack

    l = np.array([1, 2, 3])
    m = np.array([4, 5, 6])

    n = np.vstack((l, m))

    print(f"First array: {l}")
    print(f"Second array: {m}")
    print(f"Array concatenated by hstack: {n}\n")

    # Stacking along height: dstack

    o = np.array([1, 2, 3])
    p = np.array([4, 5, 6])

    q = np.dstack((o, p))

    print(f"First array: {o}")
    print(f"Second array: {p}")
    print(f"Array concatenated by dstack: {q}\n")

def split_array():

    # split is the reverse operation of join

    a = np.array([1,2,3,4,5,6])
    b = np.array_split(a,4) # there's also split() available but it will not adjust the elements when elements are less in source array for splitting

    print(f"Array: {a}")
    print(f"Splitted array: {b}")
    print(f"First section of array: {b[0]}\n")

    c = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    d = np.array_split(c, 3)

    print(f"2D Array: {c}")
    print(f"Splitted array: {d}\n")

    # Split the 2-D array into three 2-D arrays along rows.

    e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    f = np.array_split(e, 3, axis=1)

    print(f"2D Array: {e}")
    print(f"Splitted array (using axis = 1): {f}\n")

    print("Similar alternates to hstack(), vstack() and dstack() are available as hsplit(),vsplit() and dsplit().")

def search_sort_filter_array():

    #Array search

    print("Array search \n")
    arr = np.array([1,2,3,4,2,3,4,2,4])

    arr_indices = np.where(arr == 4)

    print(f"Array: {arr}")
    print(f"Indices of 4 elements in array: {arr_indices}\n")

    #searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

    a = np.array([6, 7, 8, 9])
    b = np.searchsorted(a, 7, side="left") #side part is optional, you could search for multiple numbers (instead of 7 there would be an array of elements)


    print(f"Array: {a}")
    print(f"Index of number 7: {b}")
    print("--------------\n")

    #Array sort

    print("Array sort\n")

    d = np.array([[4,7,1],[9,3,2]])
    sorted = np.sort(d)

    print(f"Array: {d}")
    print(f"Sorted array: {sorted}")
    print("--------------\n")

    #Array filter

    print("Array filter\n")

    e = np.array([1,2,3,4,5,6,7,8,9])
    filter = e%2==0

    # Same way to do the filtering

    #filter = []
    # for x in e:
    #     if (x%2==0):
    #         filter.append(True)
    #     else:
    #         filter.append(False)

    f = e[filter]

    print(f"Array: {e}")
    print(f"Array filtered by even numbers: {f}")

def main():
    #create_arrays()
    #plot_arrays()
    #data_type()
    #copy_view_array()
    #shape_array()
    #iteration_array()
    #join_array()
    #split_array()
    search_sort_filter_array()

if __name__ == "__main__":
    main()
