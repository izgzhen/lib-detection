import os, subprocess
import sys

def getLibraryLibd(path_to_apk, word_to_frequency):
    res = set()
    with open(path_to_apk, 'r') as file:
        line = file.readline()
        while not line.startswith("Time"):
            line = file.readline()
        file.readline()
        line = file.readline()
        while line:
            # get rid of the backslash at the end of the package name
            package = line.strip()[:-1]
            res.add(package)
            word_to_frequency[package] = word_to_frequency.get(package, 0) + 1
            line = file.readline()
    file.close()
    return res


def getLibraryLibRadar(path_to_apk, word_to_frequency):
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
                word_to_frequency[package] = word_to_frequency.get(package, 0) + 1
            line = file.readline()
    file.close()
    return res


def findIntersection(libdRes, libradarRes, word_to_frequency):
    """ check if they are substring of each other """
    res = list(libdRes & libradarRes)

    libdRes_leftOut = [value for value in libdRes if value not in res] 
    libradarRes_leftOut = [value for value in libradarRes if value not in res] 

    print("The intersections are: ")
    print(res)
    print("The libraries that are not in the intersection for libd are: ")
    for library in libdRes_leftOut:
        print(library + ', the relative frequency is ' + str(word_to_frequency[library]))
    print("\n")
    print("The libraries that are not in the intersection for libdradarRes are: ")
    for library in libradarRes_leftOut:
        print(library + ', the relative frequency is ' + str(word_to_frequency[library]))
    print("\n")
    return res


def main() :
    """ usage: python getLibrary.py output_folder_libd output_folder_libradar"""
    path_libd = str(sys.argv[1])
    path_libradar = str(sys.argv[2])
    files_libd = subprocess.Popen(["ls", path_libd], stdout=subprocess.PIPE)

    file_names_libd = files_libd.stdout
    word_to_frequency = dict()

    apk_to_res = dict()
    for apk_sample in file_names_libd:
        libdRes = getLibraryLibd(path_libd + apk_sample.strip(), word_to_frequency)
        libradarRes = getLibraryLibRadar(path_libradar + apk_sample.strip(), word_to_frequency)
        apk_to_res[apk_sample] = (libdRes, libradarRes)
    
    # find intersection
    for apk_sample in apk_to_res:
        libd_libradar = apk_to_res[apk_sample]
        findIntersection(libd_libradar[0], libd_libradar[1], word_to_frequency)


if __name__ == "__main__":
    main()
