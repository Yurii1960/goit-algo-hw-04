

def get_cats_info(path):
    file_name=path.name
    try:
        with open(file_name,'r',encoding='utf-8',) as fh:
           
            cats_info=[]
            info_one_cat={}
            info_all_cats=fh.readlines()
            
            
            
            for info_cat in info_all_cats :
                id,name,age=info_cat.split(',')
                info_one_cat={'id':f'{id}','name':f'{name}','age':f'{age.strip()}'}
                
                cats_info.append(info_one_cat)
            print(cats_info)
    except FileNotFoundError:
        print(f'Файл не знайдено')
