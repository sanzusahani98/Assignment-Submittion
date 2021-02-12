#Question 1
#You all are pilots, you have to land a plane, the altitude required for landing a plane is 1000ft, if itis less than that tell the pilot to land the plane, or it is more than that but less than 5000ft ask thepilot to "come down to 1000ft", else if it is more than 5000ft ask the pilot to "go around and trylater"

altitude=1000 #enter any no. in altitude

if altitude < 1000:
  print('safe land')
  elif altitude > 1000 and altitude<5000:
    print('bring down to 1000')
    else:
      print('turn around')