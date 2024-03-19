def cal_bonus(salary):
    return salary * 0.5
def cal_total_sal(salary = 50000, yos = 1):
    if yos > 5:
        bonus = cal_bonus(salary)
        print(f"salary after bonus: {salary + bonus}")
    else:
        print(f"salary without bonus: {salary}")
        
cal_total_sal(yos=10, salary=75000)