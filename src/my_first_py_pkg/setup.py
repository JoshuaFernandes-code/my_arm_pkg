import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_first_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joshua-fernandes',
    maintainer_email='joshua-fernandes@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_first_py_pkg.simple_node:main',
            'my_sub = my_first_py_pkg.subscriber_node:main',
            'service_server = my_first_py_pkg.service_server_node:main',
            'service_client = my_first_py_pkg.service_client_node:main',
            'tf_broadcaster = my_first_py_pkg.tf_broadcaster_node:main',
            'tf_listener = my_first_py_pkg.tf_listener_node:main',
            'lifecycle_node = my_first_py_pkg.lifecycle_node:main',
        ],
    },
)
