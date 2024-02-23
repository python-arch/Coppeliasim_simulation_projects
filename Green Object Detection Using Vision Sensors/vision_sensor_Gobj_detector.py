from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import os
import cv2 , numpy

# Funtion to get the centroid of the green object if found
def track_green_object(image):
    if image is None:
        return None

    # Convert the image to BGR format if it's not already
    if len(image.shape) == 3 and image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(image, (5,5),0)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image for only green colors
    lower_green = numpy.array([40,70,70])
    upper_green = numpy.array([80,200,200])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Blur the mask
    bmask = cv2.GaussianBlur(mask, (5,5),0)

    # Take the moments to get the centroid
    moments = cv2.moments(bmask)
    m00 = moments['m00']
    centroid_x, centroid_y = None, None
    if m00 != 0:
        centroid_x = int(moments['m10']/m00)
        centroid_y = int(moments['m01']/m00)

    # Assume no centroid
    ctr = None

    # Use centroid if it exists
    if centroid_x != None and centroid_y != None:
        ctr = (centroid_x, centroid_y)
    return ctr


client = RemoteAPIClient()
sim = client.getObject('sim')
# get the vision sensors handle
v_0_handle = sim.getObject('/Cuboid1/Revolute_joint/Cuboid0/v0')
v_1_handle = sim.getObject('/v1')
# empty the output directory at first
file_list = os.listdir('output')
for file_name in file_list:
    file_path = os.path.join('output', file_name)
    os.remove(file_path)
# choose the time of simulation in seconds
s_t = input("Enter simulation time:")
# start the simulation
sim.startSimulation()
while (t := sim.getSimulationTime()) < int(s_t):
    s = f'Simulation time: {t:.2f} [s]'
    # get the image buffer from the vision sensor
    image_buffer,res= sim.getVisionSensorImg(v_0_handle , 0 , 0.5,[0,0])
    # extract the resolution
    resolutionX, resolutionY = res
    # convert the image from byte string to u-int
    image = sim.unpackUInt8Table(image_buffer)
    # turn to numpy array
    image = numpy.array(image, dtype=numpy.uint8)
    image = image.reshape((resolutionY, resolutionX, 3))  # Assuming RGB image
    # find green objects
    ret = track_green_object(image)
    # for debugging
    print(ret)
    #if found green object
    # overlay rectangle marker if something is found by OpenCV
    if ret:
        cv2.rectangle(image,(ret[0]-15,ret[1]-15), (ret[0]+15,ret[1]+15), (0xff,0xf4,0x0d), 1)
        # save the output images
        # Ensure the output directory exists
        os.makedirs('output', exist_ok=True)
        # Save the image with rectangles
        output_path = os.path.join('output', f'image_at{ t}.jpg')
        cv2.imwrite(output_path , image)
    # save the image to the vision sensor 1
    image = image.tobytes()
    # write the image back
    sim.setVisionSensorImg(v_1_handle,image)
    # keep track of time
    print(s)
sim.stopSimulation()