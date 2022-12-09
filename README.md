# PongBot

<h2>Computer vision</h2>
Computer vision part of the project uses open-source python library called ImageAI (v2.1.6). Program is trained to recognise sport balls (Ping Pong balls) using pre-trained image recognition model and to display them and their relative position on the screen using OpenCV. 
<br></br>
More information about ImageAI<br>
GitHub page: https://github.com/OlafenwaMoses/ImageAI </br>
<br>Documentation: https://imageai.readthedocs.io </br>

<h3>Dependencies</h3>

- at least Python 3.7.6
- Tensorflow 2.4.0 (GPU version recommended)
- OpenCV
- Keras 2.4.3

<h3>Model</h3>

To run the program you need to download or create a object recognition model. We used ready made model RetinaNet version 2.1.0. linked in the ImageAI documentation. This model was tested to be more accurate and faster on detecting PingPong balls than the YOLOv3 models that are also suggested on the ImageAI documentation.

When you have the model, set its path to variable “path_model”.

<h2>Turtlebot Navigation</h2>
<br></br>
<h3>Dependencies<h3>

follow turtle bot and 3d vision bring up at http://wiki.ros.org/turtlebot_bringup/Tutorials/indigo/TurtleBot%20Bringup your computer need to be installed with ROS kinetic or above to execute the code. you will also need to modify your ~/.bashrc and setup.bash file located in devel folder.

<h3>How to run code</h3>

Go to the src folder and run: rosrun turtlebot turtlebot.py
