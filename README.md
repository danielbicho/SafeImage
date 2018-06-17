SafeImage
=========

SafeImage is a project that provides ways to classify images content as NSFW (Not Safe for Work).

SafeImage is composed by two components:

1. An REST WebService API provided by Flask Framework.
2. Deep Neural Networks models to classify images, ResNet and SqueezeNet.
3. Classification Workers to classify images from a Redis Queue.

Currently reported classification evaluation against the evaluation dataset:

Resnet Model

![](https://github.com/arquivo/SafeImage/blob/master/docs/ROC_OpenNSFW.pdf?raw=true "ResnetNSFW ROC")

SqueezeNet Model

![](https://github.com/arquivo/SafeImage/blob/master/docs/ROC_NsfwSqueeze.pdf?raw=true "SqueezeNetNSFW ROC")


Get code from Repository
------------------------

``` sourceCode
git clone https://github.com/arquivo/SafeImage.git
```

Install Requirements
--------------------
1. Install SafeImage API:

``` sourceCode
python setup.py install
```

Launch SafeImage API through uWSGI:
----------------------------------

``` sourceCode
uwsgi uwsgi.ini
```

Launch a classification worker through command line:
safe-image-worker

Example of request to the API:
------------------------------
Request a POST to /safeimage path with the following JSON content:

POST /safeimage

{

  "image": image_64
  
}

Replace 'image_64' with the base64 encoded image bytes.






