from mainfunctions import queryMyIP, openCacheFile, readJsonFile, writeIPtoJsonFile, GLOBAL_EXIT_CODE

def main():
    #Step 1: query my current IP address.
    current = queryMyIP()

    #Step 2: check aginst local cache.
    file = openCacheFile('IPAgent.json')
    json = readJsonFile(file)
    if(json == None):
        #Step 3: if there is no match between 1 and 2, push 1/2 into cloud provider fw.
        writeIPtoJsonFile(current)
    else:
        #close all and bye
        print()

    file.close()

if __name__ == "__main__":
    main()