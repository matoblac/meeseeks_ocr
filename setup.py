from setuptools import setup, find_packages

setup(
    name="meeseeks_ocr",
    version="0.1.0",
    description="A Docker-based CLI tool to OCR scanned PDFs into readable text.",
    author="Matt Black",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pytesseract",
        "pdf2image",
        "Pillow",
        "opencv-python",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "meeseeks-ocr=meeseeks_ocr.summon:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License"
    ]
)
