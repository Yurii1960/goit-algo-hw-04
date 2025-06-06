from pathlib import Path

def total_salary(path):
    file_name=path.name
    try:
        with open(file_name,'r',encoding='utf-8',) as fh:
           
            total=0
            person_salarys=fh.readlines()
            for salary in person_salarys:
                _,salary=salary.split(',')
                
                total=total+float(salary)
            average=total/len(person_salarys)
            
            
            
            print(f'Загальна сумма заробітної плати={total},Середня заробітна плата={average}')
            return (total,average)
    except FileNotFoundError:
        print(f'Файл не знайдено')
