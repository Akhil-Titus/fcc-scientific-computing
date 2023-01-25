"""	add_time("3:00 PM", "3:10")
	# Returns: 6:10 PM

	add_time("11:30 AM", "2:32", "Monday")
	# Returns: 2:02 PM, Monday

	add_time("11:43 AM", "00:20")
	# Returns: 12:03 PM

	add_time("10:10 PM", "3:30")
	# Returns: 1:40 AM (next day)

	add_time("11:43 PM", "24:20", "tueSday")
	# Returns: 12:03 AM, Thursday (2 days later)

	add_time("6:30 PM", "205:12")
	# Returns: 7:42 AM (9 days later) """

def add_time(start, duration, day=None):

   new_time = ''
   day_map = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }

   # data from start
   time_1,day_time = start.split()
   hour_,minutes_ = time_1.split(":")
   hour_,minutes_ = int(hour_), int(minutes_)

   if day_time == "PM":
        hour_ += 12

        

   #data from duration
   duration_hour,duration_minutes = duration.split(":")
   duration_hour,duration_minutes = int(duration_hour), int(duration_minutes)

   #Calculating total hours and minutes
   total_minutes = minutes_ + duration_minutes
   final_minutes = total_minutes % 60
   extra_hours = total_minutes // 60
   total_hour = hour_ + duration_hour + extra_hours

   # final hours as in 12 Hour format
   final_hour = (total_hour % 24) % 12

   if final_hour == 0:
        final_hour = 12
   final_hour = str(final_hour)     

   # prparing for final answer format   
   if final_minutes<=9:
     final_minutes = '0' + str(final_minutes)
   else:
      final_minutes = str(final_minutes) 

   final_day_time = ''
   if (total_hour % 24) <= 11:
     final_day_time = 'AM' 
   else:
      final_day_time = 'PM' 

  


   # original time format
   final_time = final_hour + ':' + final_minutes +' ' + final_day_time


   total_days = (total_hour // 24)
   if day == None:
        if total_days == 0:
            return final_time
        if total_days == 1:
            return final_time + ' (next day)'
        return final_time + ' (' + str(total_days) + ' days later)' 
   else:
      final_day = (day_map[day.lower().capitalize()] + total_days) % 7
      for i, j in day_map.items():
         if j == final_day:
           final_day = i
           break  
      if total_days == 0:
            return final_time + ', ' + final_day
      if total_days == 1:
         return final_time + ', ' + final_day + ' (next day)'
      return final_time + ', ' + final_day + ' (' + str(total_days) + ' days later)'           

  

   return final_time


