[app]

# (str) Title of your application
title = My App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source directory where your main.py is
source.dir = .

# (str) Version of your application
version = 1.0

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Requirements
requirements = python3,kivy

# (str) Android API level (21 = Android 5.0)
android.minapi = 21
android.targetsdk = 29

# (list) Permissions
android.permissions = INTERNET

# (str) Architecture (armv7 = 32-bit)
android.archs = armeabi-v7a

# (str) NDK version for 32-bit compatibility
android.ndk = 23b

# (bool) Use Android SDK 2
android.use_sdk2 = True

# (str) Icon of the application
# icon.filename = icon.png

# (str) Presplash of the application
# presplash.filename = presplash.png

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Gradle dependencies (leave empty for basic)
android.gradle_dependencies =

# (list) Java source files to add
android.add_src =

# (list) Java jar files to add
android.add_jars =

# (list) Python modules to include
android.add_python_modules =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Warn if run as root
warn_on_root = 1

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output
# bin_dir = ./bin

# (str) Path to Android SDK directory
# android_sdk_dir =

# (str) Path to Android NDK directory
# android_ndk_dir =

# (str) Path to Java JDK directory
# android_java_dir =

# (bool) Use Android SDK 2 (API 21+)
android.use_sdk2 = True
