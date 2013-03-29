WD := $(shell pwd)
KIVY_PROJECT_DIR := $(WD)/saythis-kivy-intro-app
PYTHON_FOR_ANDROID := $(WD)/python-for-android
PYTHON_FOR_ANDROID_PACKAGE := $(PYTHON_FOR_ANDROID)/dist/default

# Android settings
APK_PACKAGE := com.example.saythistutorial
APK_NAME := "Say This Tutorial"
APK_VERSION := 1.1.3
APK_ORIENTATION := portrait
APK_ICON := $(WD)/resources/icon.png
APK_PRESPLASH := $(WD)/resources/presplash.jpg
APK_DEBUG := $(PYTHON_FOR_ANDROID_PACKAGE)/bin/SayThisTutorial-$(APK_VERSION)-debug.apk
APK_RELEASE := $(PYTHON_FOR_ANDROID_PACKAGE)/bin/SayThisTutorial-$(APK_VERSION)-release-unsigned.apk
APK_FINAL := $(PYTHON_FOR_ANDROID_PACKAGE)/bin/SayThisTutorial.apk
APK_KEYSTORE := ~/keystores/my.keystore
APK_ALIAS := myalias

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
	./build.py --package $(APK_PACKAGE) --name $(APK_NAME) --version $(APK_VERSION) --orientation $(APK_ORIENTATION) --icon $(APK_ICON) --presplash $(APK_PRESPLASH) --dir $(KIVY_PROJECT_DIR) debug

.PHONY: package_android_release
package_android_release:
	cd $(PYTHON_FOR_ANDROID_PACKAGE); \
	./build.py --package $(APK_PACKAGE) --name $(APK_NAME) --version $(APK_VERSION) --orientation $(APK_ORIENTATION) --icon $(APK_ICON) --presplash $(APK_PRESPLASH) --dir $(KIVY_PROJECT_DIR) release
	make sign_android

.PHONY: install_android
install_android:
	adb install -r $(APK_DEBUG)

.PHONY: sign_android
sign_android:
	rm $(APK_FINAL)
	jarsigner -verbose -sigalg MD5withRSA -digestalg SHA1 -keystore $(APK_KEYSTORE) $(APK_RELEASE) $(APK_ALIAS)
	zipalign -v 4 $(APK_RELEASE) $(APK_FINAL)
