def read_data(file_name = "stu_results.csv"):
    stu_data = {}
    with open(file_name, "r") as file:
        is_first_line = 1
        for line in file:
            if is_first_line:
                is_first_line = 0
                continue
            temp_data = line.strip().split(",")
            stu_data[int(temp_data[0])] = temp_data[1:]
    return stu_data

def find_avg_sub(stu_data):
    count, math, sci, eng = 0, 0, 0, 0
    avg_sub = {}
    for stu_id in stu_data:
        count += 1
        data = stu_data[stu_id]
        math += int(data[1])
        sci += int(data[2])
        eng += int(data[3])
    avg_sub['math'] = math / count;
    avg_sub['sci'] = sci / count;
    avg_sub['eng'] = eng / count;
    return avg_sub

def find_avg_stu(stu_data):
    avg_stu = {}
    for stu in stu_data:
        sum = 0
        marks = stu_data[stu][1:]
        for mark in marks:
            sum += int(mark)
        avg_stu[stu] = sum / 3
    return avg_stu

def document(subjects, stu_data, avg_sub, avg_stu):
    print("subject statistics | average marks for each sub.")
    for subject in subjects:
        print(f"{subject} | {avg_sub[subject]}")
    print()
    
    print("student statistics | average marks for each stu.")
    for stu in stu_data:
        print(f"{stu_data[stu][0]} | {avg_stu[stu]:.2f}")

def main():
    subs = ['math', 'sci', 'eng']
    stu_data = read_data()
    avg_sub = find_avg_sub(stu_data)
    avg_stu = find_avg_stu(stu_data)
    document(subs, stu_data, avg_sub, avg_stu)
main()
