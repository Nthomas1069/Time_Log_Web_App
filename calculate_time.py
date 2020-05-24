def calculate_times(in1, out1, in2, out2, in3, out3):
   first_in = int(in1)
   second_in = int(in2)
   third_in = int(in3)
   first_out = int(out1)
   second_out = int(out2)
   third_out = int(out3)
   first_minutes = 0
   second_minutes = 0
   third_minutes = 0
   total_hours = 0
   total_minutes = 0
   invalidCount = 0
   result = ''

   # Convert to Military Time Values
   if (first_out < first_in):
      first_out += 1200

   if (second_out < second_in):
      second_out += 1200

   if (third_out < third_in):
      third_out += 1200

   # Verify Input Times are Valid
   invalidCount += checkValues(first_in)
   invalidCount += checkValues(first_out)
   invalidCount += checkValues(second_in)
   invalidCount += checkValues(second_out)
   invalidCount += checkValues(third_in)
   invalidCount += checkValues(third_out)



   # Convert Raw Times Values to Minutes
   first_minutes = calculateMinutes(first_in, first_out)
   second_minutes = calculateMinutes(second_in, second_out)
   third_minutes = calculateMinutes(third_in, third_out)

   total_minutes = first_minutes + second_minutes + third_minutes

   while (total_minutes >= 60):
      total_minutes -= 60
      total_hours += 1

   if (invalidCount == 0):
      result = 'You worked ' + str(total_hours) + ' hours and ' + str(total_minutes) + ' minutes.'
   else:
      result = 'ERROR! There are ' + str(invalidCount) + ' invalid time values.'

   return result



### Method to validate time values. ###
def checkValues(time):
   isValid = 0

   if (time % 100 >= 60):
      isValid = 1
   elif (time > 2359):
      isValid = 1

   return isValid


### Method to calculate single clock in/out time ###
def calculateMinutes(clockIn, clockOut):
   hoursInMinutes = (int(clockOut / 100) - int(clockIn / 100)) * 60
   firstMinutes = clockIn % 100
   secondMinutes = clockOut % 100
   totalMinutes = hoursInMinutes - firstMinutes + secondMinutes

   return int(totalMinutes)
