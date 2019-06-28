from setuptools import setup

setup(
    name="XRP Ledger UNL Parser",
    version="1.0",
    description="Parse published XRP Ledger Unique Node Lists (UNLs)",
    license="GNU GPL 3.0",
    author="crypticrabbit",
    author_email="postmaster@rabbitkick.club",
    packages=['parse_unl'],
    install_requires=['requests'],
)
