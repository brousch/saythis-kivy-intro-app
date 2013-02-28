#!/bin/sh

BASE_PATH=`pwd`
PACKAGE=net.clusterbleep.saythis
APP_NAME="Say This"
VERSION=1.0
BUILD_PATH=$BASE_PATH/python-for-android/dist/default
PROJECT_PATH=$BASE_PATH/saythis
DEBUG=debug
ORIENTATION=portrait
ICON=$BASE_PATH/resources/icon.png
APK=$BUILD_PATH/bin/SayThis-$VERSION-debug.apk

rm -rf $BUILD_PATH/bin
cd $BUILD_PATH
./build.py --package $PACKAGE --name "$APP_NAME" --version $VERSION --dir $PROJECT_PATH --icon $ICON --orientation $ORIENTATION $DEBUG
adb install -r $APK

