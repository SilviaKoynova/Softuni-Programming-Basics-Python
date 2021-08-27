hour_of_exam = int(input())
min_of_exam = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())
time_of_exam_in_min = hour_of_exam * 60 + min_of_exam
time_of_arrival_in_min = hour_of_arrival * 60 + min_of_arrival
difference = abs(time_of_exam_in_min - time_of_arrival_in_min)
if time_of_arrival_in_min > time_of_exam_in_min:
    print("Late")
elif time_of_exam_in_min - 30 <= time_of_arrival_in_min <= time_of_exam_in_min:
    print("On time")
elif time_of_arrival_in_min < time_of_exam_in_min - 30:
    print("Early")
if time_of_exam_in_min -60 < time_of_arrival_in_min < time_of_exam_in_min:
     print(f"{difference} minutes before the start")
elif time_of_arrival_in_min <= time_of_exam_in_min - 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes <= 9:
        print(f"{hours}:0{minutes} hours before the start ")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_exam_in_min < time_of_arrival_in_min < time_of_exam_in_min + 60:
    print(f"{difference} minutes after the start")
elif time_of_arrival_in_min >= time_of_exam_in_min + 60:
    hours = difference // 60
    minutes = difference % 60
    if minutes <=9:
        print(f"{hours}:0{minutes} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")
