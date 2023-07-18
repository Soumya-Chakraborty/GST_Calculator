from setuptools import setup, find_packages

setup(
    name='gst_calculator',
    version='1.0.0',
    description='GST calculator with GUI using tkinter',
    author='Soumya Chakraborty',
    author_email='soumyachakraborty198181@gmail.com',
    url='https://github.com/yourusername/gst_calculator',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlite3',
        'tkinter',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
