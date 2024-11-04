

#using split function to split user input according to space
#using map to convert each string to integer after splitting
array = list(map(int, input("Enter list of integers: ").split()))

#generate peak list
peaks = []

#create peaks function that find the peaks value by comparing i with its neighbors
# which i  we initialize it with index 1 
def find_peaks(array):
     for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            peaks.append(array[i])
     return peaks 
