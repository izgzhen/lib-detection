import os, subprocess
import sys
import glob
from collections import Counter

def get_library_libd(path_to_apk, total_libraries):
    res = set()
    with open(path_to_apk, 'r') as file:
        line = file.readline()
        while not line.startswith("Time"):
            line = file.readline()
        file.readline()
        line = file.readline()
        while line:
            # get rid of the backslash at the end of the package name
            line = line.strip()
            package = line
            if line[-1] == '/':
                package = package[:-1]
            res.add(package)
            total_libraries.append(package)
            line = file.readline()
    file.close()
    return res


def get_library_libRadar(path_to_apk, total_libraries):
    res = set()
    with open(path_to_apk, 'r') as file:
        line = file.readline()
        line = file.readline()
        while line:
            line = line.strip()
            if line.startswith("\"Package\""):
                # get rid of double quotes around package
                package = line.split(": \"")[1][:-2]
                res.add(package)
                total_libraries.append(package)
            line = file.readline()
    file.close()
    return res


def findIntersection(apk_name, libd_res, libradar_res, word_to_frequency):
    """find the intersection of the parsed libraries from libd and libradar"""

    res = list(libd_res & libradar_res)

    libd_res_leftOut = [value for value in libd_res if value not in res] 
    libradar_res_leftOut = [value for value in libradar_res if value not in res] 
    print("Finding the overlapping libraries on " + apk_name)
    print("The intersections are: ")
    print(res)
    print("The libraries that are not in the intersection for libd are: ")
    for library in libd_res_leftOut:
        print(library + ', the frequency is ' + str(word_to_frequency[library]))
    print("\n")
    print("The libraries that are not in the intersection for libradar are: ")
    for library in libradar_res_leftOut:
        print(library + ', the frequency is ' + str(word_to_frequency[library]))
    print("\n")


def main() :
    """ usage: python getLibrary.py output_folder_libd output_folder_libradar"""
    path_libd = sys.argv[1]
    path_libradar = sys.argv[2]
    file_names_libd = glob.glob(path_libd + "*.txt")
    file_names_libradar = glob.glob(path_libradar + "*.txt")
    
    # find the common apk files between two result folders
    file_names_libd = [i.split(path_libd)[1] for i in file_names_libd]
    file_names_libradar = [i.split(path_libradar)[1] for i in file_names_libradar]
    common_file_names = [value for value in file_names_libd if value in file_names_libradar] 

    # parsed the libraries, count the library and its frequency in the entire dataset
    total_libraries = []
    apk_to_parsed_libraries = dict()
    for apk_sample in common_file_names:
        libd_res = get_library_libd(path_libd + apk_sample.strip(), total_libraries)
        libradar_res = get_library_libRadar(path_libradar + apk_sample.strip(), total_libraries)
        apk_to_parsed_libraries[apk_sample] = (libd_res, libradar_res)
    library_to_frequency = Counter(total_libraries)
    
    # find intersection
    for apk_name, parsed_two_libraries in apk_to_parsed_libraries.items():
        libd_parsed_libraries, libradar_parsed_libraries = parsed_two_libraries
        findIntersection(apk_name, libd_parsed_libraries, libradar_parsed_libraries, library_to_frequency)


if __name__ == "__main__":
    main()
