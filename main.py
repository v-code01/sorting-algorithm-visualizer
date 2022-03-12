from sorting_algorithms import *
from random import randint
#Algorithms included:
"""
1.Bubble Sort
2.Selection Sort
3.Insertion Sort
4.Quick Sort
5.Merge Sort
6.Counting Sort
7.Radix Sort
"""
array_choices = ['Bubble Sort', "Insertion Sort", 'Insertion Sort', "Quick Sort", 'Merge Sort', "Counting Sort", 'Radix Sort']
given_array = []
def generate_arr():
    for n in range(int(input("Enter how many numbers to sort: "))):
        given_array.append(randint(1,500))
    print("The array to sort is: \n")
    print(given_array)
def call_sort_method():
    #add all the calls over here
    bubble_sort(given_array)
    print("Starting Visualization")
def visualize():
    #visualization happens in the tkinter window as a bar graph of all the array is constantly updated and shown
    #choose function and see it work!
    print("Choose a function to sort the array\n")
    print("1.Bubble Sort\n2.Selection Sort\n3.Insertion Sort\n4.Quick Sort\n5.Merge Sort\n6.Counting Sort\n7.Radix Sort")
    sorting_choice = int(input())
    print("You chose: " + array_choices[sorting_choice-1])
    call_sort_method()
generate_arr()
visualize()
