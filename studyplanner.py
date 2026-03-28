from datetime import datetime, timedelta
import matplotlib.pyplot as plt

a=int(input('enter no.of subjects:')) 
subjects=[] 
exam_dates=[] 
for i in range (a): 
    sub=input('enter subject:') 
    date = input("enter exam date (YYYY-MM-DD): ") 

    subjects.append(sub)
    exam_dates.append(datetime.strptime(date, "%Y-%m-%d").date())


slots = int(input("Enter subject per day: ")) 
today = datetime.today().date()

data = [] #combining and sorting the lists 
for i in range(a):
    data.append([subjects[i],exam_dates[i]]) 

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i][1]>data[j][1]:
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
schedule = {}
subject_count = {}

for item in data:
    subject=item[0]
    exam_date=item[1]
    days_left=(exam_date-today).days


    if days_left<=0:
        continue
    for i in range(days_left):
        day=str(today+timedelta(days=i)) 

        if day not in schedule:
            schedule[day]=[]

        if len(schedule[day]) < slots:
            schedule[day].append(subject)

            if subject not in subject_count:
                subject_count[subject]=0
            subject_count[subject]=subject_count[subject]+1 

print('\nSTUDY PLAN\n') 
print('DATE | SUBJECTS') 
print('...........................')

for day in schedule:
    print(day,'|',','.join(schedule[day])) 

subjects_list =list(subject_count.keys()) 
values=list(subject_count.values()) 

plt.figure()
plt.bar(subjects_list,values)
plt.xlabel('subjects')
plt.ylabel('studycount')
plt.title('study distribution') 
plt.show()
