from setuptools import setup
import os
from glob import glob

package_name = 'fixposition_orientation'


setup(
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='runze',
    maintainer_email='487844521@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fixposition_orientation_node = fixposition_orientation.fixposition_orientation_node:main'
        ],
    },
)
