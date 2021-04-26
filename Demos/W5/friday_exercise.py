#first

def observed():
  observations = {"Flying car", "Sky scraper", "Laser", "Done"}

  
  return observations

def run():
  print(observed())
  
run()


#
#
##
###
################# exercise
####
##
#
# second
#


def observed():
  observations = []

  for count in range(7):
    print("Please enter the observations: ")
    observations.append(input())
  return observations


def run():
  print("counting observations...")
  observations = observed()

#populate the observation items
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

    # display observation_set

  for data in observations_set:
      print(f"{data[0]} observed {data[1]} times")
run()