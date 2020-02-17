import os, subprocess
import sys

def getLibraryLibd(path_to_apk):
    res = set()
    with open(path_to_apk, 'r') as file:
        line = file.readline()
        while not line.startswith("Time"):
            line = file.readline()
        file.readline()
        line = file.readline()
        while line:
            # get rid of the backslash at the end of the package name
            res.add(line.strip()[:-1])
            line = file.readline()
    file.close()
    return res


def getLibraryLibRadar(path_to_apk):
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
            line = file.readline()
    file.close()
    return res


def findIntersection(libdRes, libradarRes):
    """ check if they are substring of each other """
    res = list(libdRes & libradarRes)

    libdRes_leftOut = [value for value in libdRes if value not in res] 
    libradarRes_leftOut = [value for value in libradarRes if value not in res] 

    print("The intersections are: ")
    print(res)
    print("The libraries that are not in the intersection for libd are: ")
    print(libdRes_leftOut)
    print("The libraries that are not in the intersection for libdradarRes are: ")
    print(libradarRes_leftOut)
    return res


def main() :
    """ usage: python getLibrary.py output_folder_libd output_folder_libradar"""
    path_libd = str(sys.argv[1])
    path_libradar = str(sys.argv[2])
    files_libd = subprocess.Popen(["ls", path_libd], stdout=subprocess.PIPE)
    files_libradar = subprocess.Popen(["ls", path_libradar], stdout=subprocess.PIPE)

    file_names_libd = files_libd.stdout
    file_names_libradar = files_libradar.stdout

    for apk_sample in file_names_libd:
        libdRes = getLibraryLibd(path_libd + apk_sample.strip())
        libradarRes = getLibraryLibRadar(path_libradar + apk_sample.strip())
        print(libdRes)
        print(libradarRes)
        # find out their intersection
        findIntersection(libdRes, libradarRes)



if __name__ == "__main__":
    main()
