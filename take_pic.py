
import picamera
import time

'''

http://picamera.readthedocs.io/en/release-1.13/
Common camera settings and defaults:

camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
'''

# setup our camera
camera = picamera.PiCamera()
camera.vflip = True
#camera.resolution = (1024, 768)

def take_picture():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    camera.capture(timestamp + '.jpg')
    print 'Snap: ' + timestamp

# crude, but we don't need precision
while True:
    take_picture()
    time.sleep(10)

