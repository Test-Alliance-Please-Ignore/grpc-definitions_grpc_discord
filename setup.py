from setuptools import setup

setup(name='grpc_discord',
    version='0.4',
    packages=['grpc_discord'],
    install_requires = [
        'grpclib',
        'googleapis-common-protos'
    ],
    zip_safe = False
)