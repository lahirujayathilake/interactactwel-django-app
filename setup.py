import setuptools

setuptools.setup(
    name="interactwel-django-app",
    version="0.0.1",
    description="InterACTWEL plugin to Airavata Django Portal",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16',
        'django-filter>=2.1.0, <2.2',
        'markdown',
        'jsonfield',
    ],
    entry_points="""
[airavata.djangoapp]
interactwel = interactwel.apps:InteractwelAppConfig
""",
)
