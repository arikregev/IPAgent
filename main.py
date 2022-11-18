from mainfunctions import queryMyIP

def main():
    #Step 1: query my current IP address.
    current = queryMyIP()
    #Step 2: Query current IP address from Cloud Provider FW.

    #Step 3: if there is no match between 1 and 2, push 1 into 2.

    print(current)

if __name__ == "__main__":
    main()