from setuptools import setup

setup(name='grpc_discord',
    version='0.7',
    packages=['grpc_discord'],
    install_requires = [
        'grpcio',
        'googleapis-common-protos'
    ],
    zip_safe = False
)