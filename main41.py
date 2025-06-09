from pathlib import Path

def total_salary(path):
    try:
        with open(path.name,'r',encoding='utf-8',) as fh:
           
            total=0
            person_salarys=fh.readlines()
            for salary in person_salarys:
                _,salary=salary.split(',')
                
                total=total+float(salary)
            average=total/len(person_salarys)
            
            return (total,average)
        
    except FileNotFoundError:
        print(f'Файл не знайдено')


