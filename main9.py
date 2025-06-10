from pathlib import Path
path=Path(r"C:\second_reposit\text.txt")


with open(path,'r',encoding='utf-8') as fh:
     person_salarys=fh.readlines()
     for salary in person_salarys:
            _,salary=salary.split(',')
            print(salary)
                
           
            
        
#path1='C:\second_reposit\text.txt'
#total_salary('C:\second_reposit\text.txt')
