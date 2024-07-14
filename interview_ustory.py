import datetime as dt
airport_data = [
  ["PDX", '-07:00'],
  ["FRA", '+02:00'],
  ["LGW", '+01:00'],
  ["BOS", '-04:00'],
  ["LAX", '-07:00'],
  ["SLC", '-06:00'],
  ["SEA", '-07:00'],
  ["SFO", '-07:00'],
  ["JFK", '-04:00']
]
format = '%H:%M'

def time_convert(time):
  new_time = dt.datetime.strptime(time,format)
  return new_time

def zone_convert(time, loc):
  for results in airport_data:
    if loc == results[0]:
      operator = results[1][0]
      numeric = results[1][1:3]
      delta = dt.timedelta(hours=int(operator+numeric)*-1)
      time_change = time + delta
  return time_change

cust_response = False

while cust_response == False:
  print("------------------------------------------------------------------------------------------------")
  print("Please input the information for your flight details below.")
  dept_time = time_convert(input("Departure Time (HH:MM): "))
  arrv_time = time_convert(input("Estimated Arrival time (HH:MM): "))
  print("Potential Airports (Select yours)")
  for zones in airport_data:
    print(zones[0])
  dept_loc = input("Departing Airport: ").upper()
  arrv_loc = input("Arriving Airport: ").upper()
  print("------------------------------------------------------------------------------------------------")
  # Confirming information with customer.
  print("Flight Data Confirmation")
  print("Please review your flight details below to confirm that the information provided is correct.")
  print("------------------------------------------------------------------------------------------------")
  print(f'Departure Details: Departing from {dept_loc} at {dept_time.time()}')
  print(f'Arrival Details: Arriving at {arrv_loc} at {arrv_time.time()}')
  print("------------------------------------------------------------------------------------------------")
  response = input("Is this information above correct? [y/n]: ").lower()
  if response == "y" or response == "yes":
    # Providing flight calculations.
    print("------------------------------------------------------------------------------------------------")
    # Calculating net departure and arrival times.
    new_dept_time = zone_convert(dept_time,dept_loc)
    new_arrv_time = zone_convert(arrv_time,arrv_loc)
    flight_time = new_arrv_time - new_dept_time
    flight_time_hours = abs(flight_time.total_seconds() / (60*60))
    flight_time_minutes = (abs((round(flight_time_hours) - flight_time_hours) * 60))+1
    # Relaying information to customer.
    print(f"Your Departure Time from {dept_loc}: {dept_time.time()}")
    print(f"You will be arriving in {arrv_loc} at: {arrv_time.time()}")
    print(f"Your flight time is: {round(int(flight_time_hours))} hour(s) and {round(int(flight_time_minutes))} minute(s).")
    print("------------------------------------------------------------------------------------------------")
    print("Enjoy your flight!")
    print("------------------------------------------------------------------------------------------------")
    cust_response = True
  else:
    print("Restarting information collection. Please provide the details regarding your flight.")
    cust_response = False