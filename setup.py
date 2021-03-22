from setuptools import find_packages, setup

setup(
    dependency_links=[],
    name="image_utils",
    version="1.0.0",
    url="https://github.com/stefantaubert/image-utils.git",
    author="Stefan Taubert",
    author_email="stefan.taubert@posteo.de",
    description="Utils for image processing",
    packages=["image_utils"],
    install_requires=[
        "imageio",
        "matplotlib",
        "numpy",
        "pillow",
        "scikit-image",
    ],
)
