from distutils.core import setup
from setuptools import find_packages

setup(
    name='SafeImage',
    version='1.0.1',
    packages=find_packages(),
    package_data={'': ['*.npy', '*.prototxt', '*.caffemodel', '*.binaryproto']},
    include_package_data=True,
    url='https://github.com/arquivo/SafeImage',
    license='',
    author='dbicho',
    author_email='daniel.bicho@fccn.pt',
    description='SafeImage Arquivo.pt Classification Tools',
    install_requires=[
        'argparse',
        'pytest',
        'PyYAML',
        'redis',
        'requests',
        'numpy',
        'tensorflow<=0.12.1',
        'Pillow',
        'flask',
        'Flask_Autodoc',
        'Flask_RESTful',
        'uwsgi',
        'scipy',
        'scikit-learn<=0.20.0',
        'scikit-image'
    ],

    entry_points={
        'console_scripts': [
            'safe-image-api=safe_image_api:main',
            'nsfw-resnet-worker=workers.resnet_nsfw_worker:main',
            'nsfw-squeezenet-worker=workers.squeezenet_nsfw_worker:main',
            'cli-safeimage-test-tool=tests.cli_models_test:main',
            'cli-safeimage-indexing=indexing.classify_images_index:main'
        ],
    },
)
