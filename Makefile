WD := $(shell pwd)
KIVY_PROJECT_DIR := $(WD)/saythis
PYTHON_FOR_ANDROID := $(WD)/python-for-android
PYTHON_FOR_ANDROID_PACKAGE := $(PYTHON_FOR_ANDROID)/dist/default

# Android settings
APK_PACKAGE := net.clusterbleep.saythis
APK_NAME := "Say This"
APK_VERSION := 1.0
APK_ORIENTATION := portrait
APK_ICON := $(WD)/resources/icon.png
APK_PRESPLASH := $(WD)/resources/presplash.jpg
APK_DEBUG := debug
APK := $(PYTHON_FOR_ANDROID_PACKAGE)/bin/SayThis-$(APK_VERSION)-debug.apk


.PHONY: run
run:
	cd $(KIVY_PROJECT_DIR); \
	python main.py

.PHONY: inspect
inspect:
	cd $(KIVY_PROJECT_DIR); \
	python main.py -m inspect

# Android commands
.PHONY: package_android
package_android:
	cd $(PYTHON_FOR_ANDROID_PACKAGE); \
	./build.py --package $(APK_PACKAGE) --name $(APK_NAME) --version $(APK_VERSION) --orientation $(APK_ORIENTATION) --icon $(APK_ICON) --presplash $(APK_PRESPLASH) --dir $(KIVY_PROJECT_DIR) $(APK_DEBUG)

.PHONY: install_android
install_android:
	adb install -r $(APK)

