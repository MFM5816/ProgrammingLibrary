import csv

with open('test.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['步惊云','绝世好剑'])
    writer.writerow(['雄霸','三分归元气'])

with open('test.csv','a') as f:
    writer = csv.writer(f)
    writer.writerows(
        [('无铭','万剑归宗'),('秦霜','天霜拳')]
    )





