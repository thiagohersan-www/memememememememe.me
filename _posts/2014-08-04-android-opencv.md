---
layout: post
title: 'Android + OpenCV = ♥ ♥ ♥'
description: using OpenCV Haar Cascade face detection on an Android phone
url: android-opencv/
date: 2014-08-04T09:47:36
cover: /assets/posts/android-opencv/android-opencv.jpg
---
![](/assets/posts/android-opencv/haarFaceTest00.png)

Finally getting our feet wet running OpenCV on an Android device... 

Good news!!! The OpenCV people have a framework that simplifies writing, compiling and running OpenCV 2.4 apps for Android devices. You no longer have to [download OpenCV source and (cross-)compile it like it's 2010](http://www.morethantechnical.com/2010/10/07/opencv2-1-on-android).

Instead, this is what we did:

**1. Installed Android SDK, NDK, and Eclipse environments and plug-ins.** 
  
There are lots of steps here, but also lots of resources online. The official [Android SDK installation guide](https://web.archive.org/web/20140730100747/http://developer.android.com/sdk/index.html), the [Android NDK installation guide](https://web.archive.org/web/20140726130201/http://developer.android.com/tools/sdk/ndk/index.html), and the [OpenCV intro to Android setup guide](http://docs.opencv.org/doc/tutorials/introduction/android_binary_package/android_dev_intro.html). 

We wanted to try out the new [Android Studio](http://developer.android.com/sdk/installing/studio.html) IDE, but as it doesn't support NDK development yet, decided to stick with Eclipse, and used the [_Manual environment setup_](http://docs.opencv.org/doc/tutorials/introduction/android_binary_package/android_dev_intro.html#manual-environment-setup-for-android-development) section of the OpenCV guide.

**2. Installed OpenCV SDK**
  
Downloaded the OpenCV 2.4 for Android library and examples from [sourceforge](http://sourceforge.net/projects/opencvlibrary/files/opencv-android/), and followed the steps in [this OpenCV setup guide](http://docs.opencv.org/doc/tutorials/introduction/android_binary_package/O4A_SDK.html).

**3. Installed OpenCV Manager app from the play store**
  
The [OpenCV Manager](https://play.google.com/store/apps/details?id=org.opencv.engine) is an app that will check for OpenCV dynamic libs already installed on a phone, and download new libraries when needed. More info is available on [this OpenCV page](http://docs.opencv.org/2.4.10/platforms/android/service/doc/index.html).

**4. RTFM (or in this case, a short guide)**
  
[This is a pretty good tutorial](http://docs.opencv.org/doc/tutorials/introduction/android_binary_package/dev_with_OCV_on_Android.html) for getting a project started: it shows how to initialize OpenCV and get frames from the camera.

After this, we tested the face detection example on some still images and on ourselves:
  
![](/assets/posts/android-opencv/haarFaceTest01.png)

Money! Even in the dark! On an old phone with Android 2.3.4!
