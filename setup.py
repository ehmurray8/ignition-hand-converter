from setuptools import setup

setup(
    name='igniton_hand_converter',
    version='0.0.1',
    description='Convert Ignition Hand History to PokerStars Hand History.',
    url='https://github.com/ehmurray8/ignition-hand-converter.git',
    author='Emmet Murray',
    author_email='ehmurray8@gmail.com',
    packages=['igconverter'],
    entry_points={
        'console_scripts': ['igconverter=igconverter.app_nogui:main']
    },
    install_requires=[
        ''
    ],
    include_package_data=True,
    zip_safe=False
)
