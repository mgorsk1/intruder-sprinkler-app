
# Configuration

## Camera

### CLS `CAMERA_CLS`

What kind of class to use for capturing images.

Default: `OpenCVCameraProvider`

### URL `CAMERA_URL`

When Open CV camera is used we can use this option to configure to either '0' (connected camera) or rtsp stream (remote web camera).

Default: `0`

### Resolution

What image size should be captured from raspberry pi camera. **In pixels.**

#### Width `CAMERA_RESOLUTION_WIDTH`

Default: `640`

#### Height `CAMERA_RESOLUTION_HEIGHT`

Default: `480`

### Framerate `CAMERA_FRAMERATE`

What's the desired video stream frame rate that should be captured.

Default: `10`

### Display `CAMERA_DISPLAY`

Should video stream be displayed during runtime.

Note that when running Garbage Detector App via SSH without GUI, this should be set to `false` or application will fail.

Default: `false`

## GCP

Configuration regarding integration with Google Cloud Platform.

### Project

#### Name `GCP_PROJECT_NAME`

Name of project where our infrastructure & services are deployed.

Default: `experiment-week`

#### Region `GCP_REGION`

Region of project where our infrastructure & services are deployed.

For several services (like AutoML, AI) this needs to be `us-central1`.

Default: `us-central1`

### Bucket

Configuration of GCP Bucket, where classification results will be stored.

#### Name `GCP_BUCKET_NAME`

Name of bucket to which save classification results.

Default: `garbage-detector-classifications`

### Vision

Settings used when our classification is done by model available in Google Cloud Platform Vision.

#### Classification

##### Threshold `GCP_VISION_CLASSIFICATION_THRESHOLD`

Accepted minimum probability of prediction made by model. Should be value from **range (0;100)**.

Default: `40`

#### Image

Size of the image we will be sending to Google Cloud Platform Vision model.

##### Size

###### Width `GCP_VISION_IMAGE_SIZE_WIDTH`

Default: `2400`

###### Height `GCP_VISION_IMAGE_SIZE_HEIGHT`

Default: `1800`

## Detector

#### Cls `DETECTOR_CLS`

Default: `GoogleCloudVisionIntruderDetector`

## Image

#### Final size `IMAGE_FINAL_SIZE`

For all classifiers (except of Google Cloud Platform Vision) the actual image will be cropped square of `IMAGE_FINAL_SIZE`
width and height. **In pixels.**

Default: `224`

#### Crop factor `IMAGE_CROP_FACTOR`

Default: `.33`


## Valve

Settings related to smart valve connected to RPI.

### GPIO `VALVE_GPIO`

To which pin power switch is connected to.

Default: `5`

## Intruder

Settings related to intruder detection

### Name `INTRUDER_NAME`

What is the name of the intruder we want to look out for.

Default: `cat`
