from setuptools import find_packages, setup

package_name = 'inspection_turtlebot4'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jaeho',
    maintainer_email='woghjaeho1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'mission_manager = inspection_turtlebot4.mission_manager:main',
        'lidar_sub = inspection_turtlebot4.lidar_sub:main',
        'image_sub = inspection_turtlebot4.image_sub:main',
        'teleop_node = inspection_turtlebot4.teleop_node:main',
        ],
    },

)
