---
layout: page
title: Freight Frenzy
subtitle: Current Season
---

<div class="sectioncontent5">
    <p align="center">Robot Overview</p>
    <br>
    <div class="freightfrenzy textleft"> 
        <img src="Overview1.png" class="freightfrenzypic" style="width:80%;">
        <img src="Overview2.png" class="freightfrenzypic" style="width:80%;">
    </div>
</div>
<div class="sectioncontent5" style="margin-top:5%">
    <p align="center">Mechanisms</p>
</div>
<div class="sectioncontent2">
    <p class="freightfrenzysub left">Drivetrain</p>
    <div class="freightfrenzy-reverse"> 
        <small class="textbox textleft">After much strategy analysis, we realized that we wanted to have a compact robot that would fit in between the barriers to optimize our scoring output. We also wanted to have easy driver navigation, and decided to use goBILDA Mecanum wheels for omni-directional movement. In order to track our robot’s positioning in autonomous, we compactly package 3 dead wheel odometry pods, designed by FTC Primitive Data, that provide accurate sensory data to our robot. To reduce the weight of our drivetrain, we created custom hole designs called pockets via CAD. These holes return the structural integrity of the plate while also providing a sleek and aesthetic design.
        </small>
        <img src="DT.png" class="freightfrenzypic">
    </div>
    <p class="freightfrenzysub right">Intake</p>
    <div class="freightfrenzy"> 
        <img src="Succ.png" class="freightfrenzypic">
        <small class="textbox textright">Based on our prior experience with wiffle balls and orange cubes from the Rover Ruckus season, we immediately realized that using a surgical tubing intake would be the quickest way for us to collect game elements. To make our intake have more leeway, we designed it to be passively mounted and constantly sprung downwards. Our intake is powered by a goBILDA 1150 RPM motor, allowing us to instantly transfer game elements to our deposit box. For space consumption purposes, we use two 1:1 bevel (miter) gears to power a coaxial shaft that serves both to transfer torque to the surgical tubing roller and to act as a pivoting shaft. The plates are made out of laser cut delrin for rigidity and lightness.
        </small>
    </div>
    <p class="freightfrenzysub left">Lift</p>
    <div class="freightfrenzy-reverse"> 
        <small class="textbox textleft">In order to reach the higher levels of the alliance shipping hubs, we designed an angled lift to provide both horizontal and vertical extension. We use Long Robotics linear slides and customly mount them together with 3D printed inserts and laser cut delrin mounts.
        Or lift is powered by a traditional string and pulley mechanism, and its unique feature is that it uses two strings. We have an extension string and a retraction string that is tied to a spring to provide constant tension to our lift, which is an extremely vital component for proper function. Using two goBILDA 5.2 motors and 50mm diameter pulley, we can power our lift with enough torque and an extremely high speed.
        </small>
        <img src="Lift.png" class="freightfrenzypic biggerpic">
    </div>
    <p class="freightfrenzysub right">Deposit</p>
    <div class="freightfrenzy"> 
        <img src="Deposit.png" class="freightfrenzypic">
        <small class="textbox textright">Our deposit mechanism essentially functions like a 2 segment arm. Two goBILDA torque servos drive laser cut delrin arm segments to move our 3D printed deposit box from inside the robot to outside the robot. A final goBILDA speed servo is used to pivot the box, allowing us to drop freight at various angles. Both our arm and box are pocketed to reduce weight and provide holes for routing wires.
        </small>
    </div>
    <p class="freightfrenzysub left">Carousel Spinner</p>
    <div class="freightfrenzy-reverse"> 
        <small class="textbox textleft">Our carousel spinner is a fairly simple mechanism. For compactness, we direct mounted a goBILDA Rhino wheel to a 435 RPm motor for maximum traction along the carousel. To find the optimal speed to provide our motor with, we simply did some trial and error testing to see when the duck would stop falling from too much momentum.
        </small>
        <img src="spin_rescale.png" class="freightfrenzypic wheel">
    </div>
</div>
<div class="sectioncontent5">
    <p align="center">Software Engineering</p>
</div>
<div class="sectioncontent2">
    <p class="freightfrenzysub right">Sensors</p>
    <div class="freightfrenzy"> 
        <img src="Censor.png" class="freightfrenzypic bigpic">
        <small class="textbox textright">Our robot has many intricate and complex algorithms to allow for effective use of our robot’s full capabilities. However, this would not be possible without the many sensors that guide our robot’s every step.
        The most complex and important use of sensors is in our dead-wheel odometry system. With three free spinning wheels attached to Rev Encoders, our robot is provided with responsive information regarding its movement. With this, we can utilize libraries like RoadRunner and utilize PID feedback loops to match the desired path with the actual path, resulting in accurate autonomous pathing.
        </small>
    </div>
    <br>
    <div class="freightfrenzy-reverse">
        <small class="textbox textleft">However, there exists many other sensors that play a key role in our robot’s mechanisms. For example, a color sensor within the deposit allows for detection of collected freight. This enable automatic outtaking to prevent further deposits from getting caught on the robot. Furthermore, encoders on the lift motors enable the use of a PID controller to precisely reach the desired height as quickly as possible.
        </small>
        <img src="Censor2.png" class="freightfrenzypic biggerpic">
    </div>
    <br>
    <div class="freightfrenzy">
        <small class="textbox" style="margin-left:2.5%; width:100%">All in all, these sensors work together to create a cohesive view of our robot, and help guide the mechanisms utilizing real-time feedback from the robot’s current status.
        </small>
    </div>
    <br>
    <p class="freightfrenzysub right">Autonomous Path Planning & Tuning Tools</p>
    <div class="freightfrenzy"> 
        <img src="idkl.png" class="freightfrenzypic biggerpic">
        <small class="textbox textright">Just like the design thinking process, path planning is a process of it’s own that requires abstraction, iteration, and definition over the course of its development. As outlined in our game strategy, our goals were created accordingly to our robot’s strengths and a path was created to take advantage of these strengths. After this basic abstraction is then implemented using a path planning tool, called MeepMeep. Once a basic path is formed, we’re able to get started on converting our vision to points.
        </small>
    </div>
</div>
