import random
import csv
def generate_cityname():
    s=""
    for i in range(1,random.randint(3,8)):
        ch = chr(64 + random.randint(1,26))
        s += ch
    # print(s)
    return s

def generate_city():
    city_list = []
    for i in range(1,10):
        c = dict(city_id = random.randint(1,6),city_name=generate_cityname(), city_code = random.randint(11,40), population = random.randint(100000,1000000)) 
        city_list.append(c)
        print(city_list)
    return city_list
generate_city()

FILE_PATH = r"G:\python1\Task_random_city_csv\city_info1.csv"

def write_csv():
    list_city = generate_city()
    # keys = list_city[0].keys()
    fieldnames = ['city_id','city_name','city_code','population']
    print(list_city)
    
    with open(FILE_PATH, 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_city)
   
write_csv()