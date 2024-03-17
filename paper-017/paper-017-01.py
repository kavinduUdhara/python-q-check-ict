def read_data():
    with open("stu_results.csv", "r") as file:
        count = 0
        for line in file:
            if count == 0:
                
            print(line.strip())
            
            
read_data()            