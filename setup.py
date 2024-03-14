from setuptools import setup

setup(
    name='aut',
    version='0.4.0',
    description='command-line RPC client for Autonity',
    url='https://github.com/autonity/aut',
    author='Autonity',
    author_email='contact@autonity.io',
    license='MIT',
    packages=['aut'],
    install_requires=[
        'boto3',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'aut=aut.__main__:main',
            'aut-shutdown=aut.shutdown:main',
            'aut-start=aut.start:main',
            'aut-status=aut.status:main',
            'aut-terminate=aut.terminate:main',
            'aut-wait=aut.wait:main',
            'aut-wait-shutdown=aut.wait_shutdown:main',
            'aut-wait-start=aut.wait_start:main',
        ],
    },
)