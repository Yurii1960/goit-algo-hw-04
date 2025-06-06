

def total_salary(path):
    try:
        with open("text.txt",'r',encoding='utf-8',) as fh:
           
            total=0
            person_salarys=fh.readlines()
            for salary in person_salarys:
                _,salary=person_salarys.split(',')
                
                total=total+float(salary)
            print(total)
            
            print(f'Загальна сумма заробітної плати={total},Середня заробітна плата={average}')
    except FileNotFoundError:
        print(f'Файл не знайдено')
