import csv

data=[
    # ["eid","name","Gender","salary","department"],
    [110,'nileesha','female',30000,'Hr'],
    [111,'tejas','male',50000,'dev'],
    [112,'vishal','male',40000,'testing']
]

with open('employee.csv','a',newline="") as f:
    write = csv.writer(f)
    # write.writerows(data)
    write.writerow([114,'amruta','female',76000,'data science'])
    write.writerow([115,'harshada','female',76000,'data science'])
    write.writerow([116,'mayuri','female',76000,'data science'])
print('written successfully')