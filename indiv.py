#######################################################
## Quickly increase and decrease each LED one by one ##
##                                                   ##
##  Example by Jason - @Boeeerb                      ##
#######################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow(1)
val = 0
count = 1
while True:
<<<<<<< HEAD
	leds = range(1,19,+1)
	for led in leds:
		if count == 1:
			val = val + 1
			if val > 90:
				count = 0
		else:
			val = val - 1
			if val < 1:
				count = 1
		piglow.led(led,val)
		

		sleep(0.0075)
=======
    leds = range(1,19,+1)
    for led in leds:
        if count == 1:
            val = val + 1
            if val > 90:
                count = 0
            else:
                val = val - 1
                if val < 1:
                    count = 1
        piglow.led(led,val)
        sleep(0.0075)
>>>>>>> a33d9a78ec20545ddbd7af4cd37e0b107fef38e0
