from setuptools import setup, find_packages

setup(
    name="u2net",
    version="0.1.0",
    description="U^2-Net for Salient Object Detection",
    # Only include the "model" package
    packages=find_packages(include=["model"]),
    install_requires=[
        "pillow>=11.0.0",
        "numpy==1.26.4",
        "opencv-python>=4.10.0.84",
        "torch",
        "torchvision",
        "scikit-image>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            # Add any other development dependencies here
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
