
import glob 
import pandas as pd 
  
# specifying the path to csv files 
path = r"filepath" ## Путь на папку (без "r" не работает(типа читать))
  
# csv files in the path 
files = glob.glob(path + "\*.csv") ## собираем файлы глобом(точно не знаю как он работает, надо узнать!!!)
  
# defining an empty list to store  (переменные на будущее)
# content 
data_frame = pd.DataFrame() 
content = [] 
  
# checking all the csv files in the  
# specified path 
for filename in files: ## Цикл по файлам в папке
    
    # reading content of csv file 
    # content.append(filename) 
    df = pd.read_csv(filename, header=None, sep='delimiter') ## без укозания дериметра будет ошибка, в данный момент он не указан, мне это не нужно
    print(len(df)) ## выводим кол-во строк
    print(filename) ## выводим название файла
    content.append(df) 

  
# converting content to data frame 
data_frame = pd.concat(content) 
print(data_frame) 