---
layout: post
title: The Dynamixel AX-12A Servos
description: using Dynamixel AX-12A servo motors
url: the-dynamixel-ax-12a-servos/
date: 2014-07-12T18:42:51
cover: /assets/posts/the-dynamixel-ax-12a-servos/the-dynamixel-ax.jpg
---
![](/assets/posts/the-dynamixel-ax-12a-servos/Hangar06.jpg)

We decided to experiment with some [Dynamixel AX-12A servos](http://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx) for this project. Despite being a little bit more expensive, this motor has a couple of advantages over the more commonly found [TowerPro motors](http://www.servodatabase.com/servo/towerpro/mg996r).

Mainly, the Dynamixel motors are stronger, daisy chainable, and have a [robust control system](http://support.robotis.com/en/techsupport_eng.htm#product/dynamixel/ax_series/dxl_ax_actuator.htm) that reports position, temperature, torque, etc...

We found two different manuals for the AX-12A motors online. [This manual](http://www.trossenrobotics.com/images/productdownloads/AX-12&#40;English&#41;.pdf) is from 2006, and is a little outdated: some of the spec values are outdated (operating voltage range, for example), and some of the initial values reported in the Control Table are not correct, but it goes into detail about how to send instructions to the motor and how to read its response.

[This other manual](http://support.robotis.com/en/techsupport_eng.htm#product/dynamixel/ax_series/dxl_ax_actuator.htm) has more accurate values for specs and initial conditions, but lacks some of the detailing of the communication protocol.

It's useful to have both of them.

Unlike other servos, the Dynamixel doesn't respond to PWM signals, but a slightly more complicated protocol of instructions for reading and writing onto its memory. This communication happens over a half-duplex UART port, using only one wire for both sending and receiving.

What this means is that we need to build a small circuit that converts full-duplex into half-duplex, if we want to use a Raspberry Pi or an Arduino (or another microcontroller with a full-duplex serial interface) to control these motors.

One of the [AX-12 manuals](http://www.trossenrobotics.com/images/productdownloads/AX-12&#40;English&#41;.pdf) recommends this circuit:
  
![](/assets/posts/the-dynamixel-ax-12a-servos/uart_manual.png)

It's basically a tri-state buffering scheme for arbitrating the bus; it makes sure that when the controller is transmitting, the bus isn't connected to the Rx pin, and that when it's expecting to receive, it's not being driven by the Tx pin.

Instead of using a 74HC126 and a 74HC04, we used a [74LS241](http://www.electronica60norte.com/mwfls/pdf/74ls241.pdf) (as recommended [here](http://savageelectronics.blogspot.it/2011/01/arduino-y-dynamixel-ax-12.html)), because it already has the built-in capability of enabling half of its buffers with a high signals, and the other half with a low signal.

Something like this:

![](/assets/posts/the-dynamixel-ax-12a-servos/uart_half-duplex_74LS241.jpg)

We first tested the circuit using an Arduino and the library found [here](http://savageelectronics.blogspot.com.es/2011/08/actualizacion-biblioteca-dynamixel.html).

But, because we might eventually want to connect our robots to the internet, or keep track of their state between reboots, or do some heavier computation... we might want to use a Raspberry Pi as the controller. We started testing [this library](https://github.com/jes1510/python_dynamixels) for controlling the motors using a Raspberry Pi, but then decide to re-write it to make it more object-oriented, and to have some of the same capabilities as the Arduino library.

Our [AX-12A Python library for Raspberry Pi is on github](https://github.com/thiagohersan/memememe/tree/master/Python/ax12).

We also designed a [simple PCB for the UART circuit](http://123d.circuits.io/circuits/267189-ax-12-driver-for-raspberry-pi/) with a Raspberry Pi header, using [123D.circuits](http://123d.circuits.io/).

![](/assets/posts/the-dynamixel-ax-12a-servos/uart_pcb.png)
