---
layout: page
title: Freight Frenzy
subtitle: Current Season
---

<div class="sectioncontent5">
    <p align="center">Robot Overview</p>
    <div style="display: flex"> 
        <img src="Overview1.png" class="center" style="width:90vh; margin-left:10%">
        <img src="Overview2.png" class="center" style="width:90vh; margin-right:10%">
    </div>
</div>
<div class="sectioncontent5" style="margin-top:5%">
    <p align="center">Mechanisms</p>
</div>
<div class="sectioncontent">
    <p class="freightfrenzypmargins" align="center">Drivetrain</p>
    <div style="display: flex"> 
        <small style="margin-left:10%; margin-right:5%">After much strategy analysis, we realized that we wanted to have a compact robot that would fit in between the barriers to optimize our scoring output. We also wanted to have easy driver navigation, and decided to use goBILDA Mecanum wheels for omni-directional movement. In order to track our robot’s positioning in autonomous, we compactly package 3 dead wheel odometry pods, designed by FTC Primitive Data, that provide accurate sensory data to our robot. To reduce the weight of our drivetrain, we created custom hole designs called pockets via CAD. These holes return the structural integrity of the plate while also providing a sleek and aesthetic design.
        </small>
        <img src="DT.png" class="center" style="width:50vh; margin-top:0%; margin-right:10%">
    </div>
    <p align="center" style="margin-top:0%">Intake</p>
    <div style="display: flex"> 
        <img src="Succ.png" class="center" style="width:60vh; margin-top:0%; margin-left:10%">
        <small style="margin-left:5%; margin-right:10%">Based on our prior experience with wiffle balls and orange cubes from the Rover Ruckus season, we immediately realized that using a surgical tubing intake would be the quickest way for us to collect game elements. To make our intake have more leeway, we designed it to be passively mounted and constantly sprung downwards. Our intake is powered by a goBILDA 1150 RPM motor, allowing us to instantly transfer game elements to our deposit box. For space consumption purposes, we use two 1:1 bevel (miter) gears to power a coaxial shaft that serves both to transfer torque to the surgical tubing roller and to act as a pivoting shaft. The plates are made out of laser cut delrin for rigidity and lightness.
        </small>
    </div>
    <p align="center" style="margin-top:0%">Lift</p>
    <div style="display: flex"> 
        <small style="margin-left:10%; margin-right:5%">In order to reach the higher levels of the alliance shipping hubs, we designed an angled lift to provide both horizontal and vertical extension. We use Long Robotics linear slides and customly mount them together with 3D printed inserts and laser cut delrin mounts.
        Our lift is powered by a traditional string and pulley mechanism, and its unique feature is that it uses two strings. We have an extension string and a retraction string that is tied to a spring to provide constant tension to our lift, which is an extremely vital component for proper function. Using two goBILDA 5.2 motors and 50mm diameter pulley, we can power our lift with enough torque and an extremely high speed.
        </small>
        <img src="Lift.png" class="center" style="width:40vh; margin-top:-7%; margin-right:10%">
    </div>
    <p align="center" style="margin-top:0%">Deposit</p>
    <div style="display: flex"> 
        <img src="Deposit.png" class="center" style="width:40vh; margin-top:-11%; margin-left:10%">
        <small style="margin-left:5%; margin-right:10%">Our deposit mechanism essentially functions like a 2 segment arm. Two goBILDA torque servos drive laser cut delrin arm segments to move our 3D printed deposit box from inside the robot to outside the robot. A final goBILDA speed servo is used to pivot the box, allowing us to drop freight at various angles. Both our arm and box are pocketed to reduce weight and provide holes for routing wires.
        </small>
    </div>
    <p align="center" style="margin-top:0%">Carousel Spinner</p>
    <div style="display: flex"> 
        <small style="margin-left:10%; margin-right:5%">Our carousel spinner is a fairly simple mechanism. For compactness, we direct mounted a goBILDA Rhino wheel to a 435 RPm motor for maximum traction along the carousel. To find the optimal speed to provide our motor with, we simply did some trial and error testing to see when the duck would stop falling from too much momentum.
        </small>
        <img src="Spinnysadsadasdsa.png" class="center" style="width:15vh; margin-top:-10%; margin-right:10%">
    </div>
</div>
<div class="sectioncontent5">
    <p align="center">Software Engineering</p>
</div>
<div class="sectioncontent">
    <p align="center">Sensors</p>
    <div style="display: flex"> 
        <img src="Censor.png" class="center" style="width:50vh; margin-top:-7%; margin-left:10%">
        <small style="margin-left:5%; margin-right:10%">Our robot has many intricate and complex algorithms to allow for effective use of our robot’s full capabilities. However, this would not be possible without the many sensors that guide our robot’s every step.
        The most complex and important use of sensors is in our dead-wheel odometry system. With three free spinning wheels attached to Rev Encoders, our robot is provided with responsive information regarding its movement. With this, we can utilize libraries like RoadRunner and utilize PID feedback loops to match the desired path with the actual path, resulting in accurate autonomous pathing.
        </small>
    </div>
    <div style="display: flex">
        <small style="margin-left:10%; margin-right:5%">However, there exists many other sensors that play a key role in our robot’s mechanisms. For example, a color sensor within the deposit allows for detection of collected freight. This enable automatic outtaking to prevent further deposits from getting caught on the robot. Furthermore, encoders on the lift motors enable the use of a PID controller to precisely reach the desired height as quickly as possible.
        </small>
        <img src="Censor2.png" class="center" style="width:40vh; margin-top:-10%; margin-right:10%">
    </div>
    <div style="display: flex">
        <small style="margin-left:10%; margin-right:10%;">All in all, these sensors work together to create a cohesive view of our robot, and help guide the mechanisms utilizing real-time feedback from the robot’s current status.
        </small>
    </div>
    <p align="center" style="margin-top:0%">Autonomous Path Planning & Tuning Tools</p>
    <div style="display: flex"> 
        <img src="idkl.png" class="center" style="width:40vh; margin-top:-7%; margin-left:10%">
        <small style="margin-left:5%; margin-right:10%">Just like the design thinking process, path planning is a process of it’s own that requires abstraction, iteration, and definition over the course of its development. As outlined in our game strategy, our goals were created accordingly to our robot’s strengths and a path was created to take advantage of these strengths. After this basic abstraction is then implemented using a path planning tool, called MeepMeep. Once a basic path is formed, we’re able to get started on converting our vision to points.
        </small>
    </div>
</div>
