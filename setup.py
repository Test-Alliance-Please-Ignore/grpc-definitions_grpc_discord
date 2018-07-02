from setuptools import setup

setup(name='grpc_discord',
    version='0.3',
    packages=['grpc_discord'],
    install_requires = [
        'grpcio',
        'grpclib',
        'googleapis-common-protos'
    ],
    zip_safe = False
)