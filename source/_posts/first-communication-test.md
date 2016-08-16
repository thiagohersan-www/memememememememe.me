---
layout: post
title: First Communication Test
description: Stewart Platform communication tests
url: first-communication-test/
date: 2014-07-28T06:28:45
cover: /assets/posts/first-communication-test/first.jpg
---
After some work doing the math and the simulator, we finally got real-time communication going between our simulator and the platform. But, not before re-orienting some of the servo horns (because the AX-12A motors only rotate about 300&deg;), and writing some code to transform angles into AX12-A motor commands.

![](/assets/posts/first-communication-test/NapkinMath01.jpg)

Here is a video with the screenshot of the simulator plus the platform.

<div class="video-wrapper video-wrapper-3x1">
  <iframe src="//player.vimeo.com/video/101919411" frameborder="0" allowfullscreen="allowfullscreen"></iframe>
</div>

The code for testing the motors using the simulator is [on github](https://github.com/thiagohersan/memememe/tree/master/Python/test-PlatformCommunication). It uses [OSC](http://opensoundcontrol.org/) to send motor angle packets to the Raspberry Pi controlling the platform.

We're still figuring out how to make the movements more continuous, as we keep improving and fixing the [servo library for python](https://github.com/thiagohersan/memememe/tree/master/Python/ax12). For example, we noticed that some commands weren't getting to the motors, and as a result we were getting timeout errors while waiting for their response. We're still not sure what causes some commands to never get to the motors (it might have something to do with the timing of the Rx/Tx direction signal), but we can decrease the number of missed commands by catching a timeout exception, and resending the command. In order for this to work we had to [decrease the serial port timeout delay in the library](https://github.com/thiagohersan/memememe/commit/81eee19f3b573922406464d665e0aa092941c198). It turns out it's better to timeout after 1ms and re-send, then to wait 500ms for a reply. Duh !

![](/assets/posts/first-communication-test/NapkinMath02.jpg)
