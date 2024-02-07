import setuptools


REQUIRED_PACKAGES = [
    'matplotlib>=2.2.3',
    'seaborn>=0.9.0',
    'scikit-learn>=1.0.2',
    'pandas',
    'numpy',
    'hdbcli',
    'pandas-gbq',
    'fedml_gcp'

]

setuptools.setup(
    name='dwc_gcp_model_v4',
    version='v4',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    include_package_data=True,
    description='dwc_gcp_model_training',
    package_data={'trainer': ['config.json']}
)