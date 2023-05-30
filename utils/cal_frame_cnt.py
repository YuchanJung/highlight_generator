file_name = "temp.txt"
new_file_name = "20220730_두산_한화"

with open(file_name, "r") as temp_file:
    with open(new_file_name, "a") as new_file:
        for line in temp_file:
            start, end = line.strip().split(",")
            start_hour, start_minute, start_second = start.split(':')
            start_hour = float(start_hour)
            start_minute = float(start_minute)
            start_second = float(start_second)
            end_hour, end_minute, end_second = end.split(':')
            end_hour = float(end_hour)
            end_minute = float(end_minute)
            end_second = float(end_second)
            
            start_frame = int(((start_hour * 60 +start_minute) * 60 + start_second) * 30)
            end_frame = int(((end_hour * 60 + end_minute) * 60 + end_second) * 30)

            content = f"{start_frame},{end_frame}, {line}"
            new_file.write(content)
