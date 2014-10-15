#test version for the robot library

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO)
#gpio

rechtsoben = GPIO.setpin(3)
rechtsmittel = GPIO.setpin(5)
rechtsunten = GPIO.setpin(7)
rechts_gesammt = [rechtsoben, rechtsmittel, rechtsunten]

linksoben = GPIO.setpin(11)
linksmittel = GPIO.setpin(13)
linksunten = GPIO.setpin(15)
links_gesammt = [linksoben, linksmittel, linksunten]

rechtsobenbw = GPIO.setpin(8)
rechtsmittelbw = GPIO.setpin(10)
rechtsuntenbw = GPIO.setpin(12)
rechts_gesammtbw = [rechtsoben, rechtsmittel, rechtsunten]

linksobenbw = GPIO.setpin(16)
linksmittelbw = GPIO.setpin(18)
linksuntenbw = GPIO.setpin(22)
links_gesammtbw = [linksoben, linksmittel, linksunten]
#die verschiedene seiten
def rechte_seite_fw(sekunde) :
    GPIO.setpin(rechtsoben, True)
    GPIO.setpin(rechtsunten, True)
    GPIO.setpin(rechtsmittel, True)
    time.sleep(sekunde)
    GPIO.setpin(rechtsmittel, False)
    GPIO.setpin(rechtsoben, False)
    GPIO.setpin(rechtunten, False)
    
def linke_seite_fw(sekunde) :
    GPIO.setpin(linksoben, True)
    GPIO.setpin(linksunten, True)
    GPIO.setpin(linksmittel, True)
    time.sleep(sekunde)
    GPIO.setpin(linksmittel, False)
    GPIO.setpin(linksoben, False)
    GPIO.setpin(linksunten, False)
# die "commands", die uns interessieren...
def fw(schritte):
    rechte_seite(schritte)
    linke_seite(schritte)
