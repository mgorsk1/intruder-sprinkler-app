# Intruder Detector

This repository consist of elements that make up Intruder - an AI-powered intruder detector setting off sprinklers in your garden whenever a certain intruder (eg. cat) shows up.

## Premise

## Architecture

### Raspberry Pi

Our intruder detector is a device powered by Raspberry Pi with several integrations, namely:

* **Rasbperry Pi Camera HD tv2** - capturing images for classification
* Smart valve to turn sprinklers on/off
* Power switch to relay 12V to Smart valve

#### Prototype



### Intruder Detector - App

The app lies within `intruder_detector`. It's a fully configurable, simple process orchestrating interaction between
user, classification mechanism and sprinkler manager.

### Classifiers

Currently following classifiers are supported:

#### [GCP Cloud Vision](https://cloud.google.com/vision/docs)

GCP Cloud Vision is a product from Google Cloud Platform providing ready-to-use state-of-the-art model for image classification and object recognition.

With this product, he classification is automatic - we query model for `object detection` predictions and look for presence of intruder category in received annotations.

### Demo

Click for the youtube video:

### Contributors
