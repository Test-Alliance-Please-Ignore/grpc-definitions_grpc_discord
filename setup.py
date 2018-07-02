from setuptools import setup

setup(name='grpc_discord',
    version='0.2',
    packages=['grpc_discord'],
    install_requires = [
        'grpcio',
        'googleapis-common-protos'
    ],
    zip_safe = False
)