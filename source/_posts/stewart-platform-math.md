---
layout: post
title: Stewart Platform Math
description: understanding the Stewart Platform
url: stewart-platform-math/
date: 2014-07-20T17:47:52
cover: /assets/posts/stewart-platform-math/stewart-platform.jpg
---
We tested our [AX-12A library](https://github.com/thiagohersan/memememe/tree/master/Python/ax12) and motor driver circuit using one of the motors attached to our platform. We quickly realized that the servos on the platform can't be driven independently of each other; in most cases, all six motors have to move simultaneously in order to achieve any desired position or pose.

This is a video showing how all the motors are affected when we drive only one motor up and down:

<div class="video-wrapper-wrapper-small">
  <div class="video-wrapper video-wrapper-16x9">
    <iframe src="//www.youtube.com/embed/rAhi5TZZJ6o?rel=0" frameborder="0" allowfullscreen=""></iframe>
  </div>
</div>
  
Before we started sending signals to all the servos, we figured it would be worthwhile to get familiar with the mathematics of the [Stewart Platform](http://en.wikipedia.org/wiki/Stewart_platform).

Unlike articulated robotic arms, the Stewart Platform's [inverse kinematics](http://en.wikipedia.org/wiki/Inverse_kinematics) are simpler than its [forward kinematics](http://en.wikipedia.org/wiki/Forward_kinematics). What this means is that it's easier to calculate the leg lengths and motor parameters given a desired position for the platform, than to calculate where the platform is located for a given set of motor parameters. This is fine; we really want the inverse kinematics anyway, and that way we avoid solving a system of 18 non-linear equations with 40 possible solutions.

Some of the papers that we found were not specific to servo-based Stewart Platforms; they simply described the math based on desired leg lengths, and sometimes assumed that linear actuators would be used. This is the case for [this paper](http://www.fields.utoronto.ca/journalarchive/mics/3-9.pdf), which describes a very specific Stewart Platform and focuses on its forward kinematics. 

We also found two papers that were more specific for servos. [This paper](http://www.techfak.uni-bielefeld.de/~fszufnar/publications/Szufnarowski2013.pdf) by Filip Szufnarowski describes the inverse kinematic problem very nicely, but it was [this document](http://tinyurl.com/wu3a-sp) by an unknown author from the [Wokingham U3A Math Group](http://www.wokinghamu3a.org.uk/groups/mathematics/) that had the most detail and cleanest notation. For example, this image that labels all the relevant points of a Stewart Platform with their corresponding coordinate system:

![](/assets/posts/stewart-platform-math/platformCoordinateSystems.png)

The inverse kinematics problem of a Stewart Platform can be broken up into two stages:

(1) Given a desired position and orientation for the platform, how far is each joint on the platform from its corresponding base joint, 

and 

(2) What servo angles, if any, put each platform joint in the positions calculated in the previous step.

The first problem is easy to solve; once you have the appropriate points and coordinate systems defined like in the above image, the distances between base joints and platforms joints can be calculated with simple matrix operations for rotation and translation.

Namely, the length of each leg is calculated as:
  
![](/assets/posts/stewart-platform-math/MatrixMath_eq_length_tgh.png)

with:
  
![](/assets/posts/stewart-platform-math/MatrixMath_eq_rot_tgh.png)

The second part, is a little bit trickier. For each servo, given a platform joint position **P**, relative to the base joint position **B**, and fixed lengths for the servo horn _a_ and support leg _s_, what is the servo arm angle that satisfies the distance _l_ calculated in the previous step.

![](/assets/posts/stewart-platform-math/ServoMath.jpg)

Since _l_ increases as you vary the servo arm angle from -90&deg; to +90&deg; (relative to base plane), one way to solve for this angle is to do a binary search over the angle values, and find the one that more closely satisfies all the distance constraints. This is done on [the code](https://github.com/ThomasKNR/RotaryStewartPlatform) for [this Stewart Platform](http://www.instructables.com/id/Arduino-controlled-Rotary-Stewart-Platform/).

But, the Wokingham U3A Math Group [document](http://tinyurl.com/wu3a-sp) actually steps through the derivation of a closed-form expression for this angle, using some pretty sweet geometry, algebra and trigonometry tricks.

SPOILER ALERT !!! SPOILER ALERT !!! SPOILER ALERT !!! SPOILER ALERT !!!
  
![](/assets/posts/stewart-platform-math/MatrixMath_angle_tgh.png)

We actually found a small bug in this part of the document. In equations (8), while calculating _l<sup>2</sup>_ and _s<sup>2</sup>_, instead of using the (_x<sub>p</sub>_, _y<sub>p</sub>_, _z<sub>p</sub>_) values for the platform joint positions in the platform coordinate system, you have to use the (_x<sub>q</sub>_, _y<sub>q</sub>_, _z<sub>q</sub>_) values, which are relative to the base coordinate system.
  
![](/assets/posts/stewart-platform-math/NapkinMath00.jpg)

We wrote a simple Stewart Platform simulator for our platform, to see the range of movements that it will be able to achieve, and to double-check the math. The code is in [Processing](http://processing.org/), and is [on github](https://github.com/thiagohersan/memememe/tree/master/Processing/StewartSimulator).

<div class="video-wrapper-wrapper-small">
  <div class="video-wrapper video-wrapper-4x3">
    <iframe src="//www.youtube.com/embed/_u-Sl9uDPj4?rel=0" frameborder="0" allowfullscreen=""></iframe>
  </div>
</div>
