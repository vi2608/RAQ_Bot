from setuptools import find_packages, setup

setup(
    name="PDF QA Bot for Privacera",
    version="0.0.1",
    author="Vipul Munot",
    author_email="vmunot23@gmail.com",
    packages =find_packages(),
    install_requires=["langchain","streamlit", "langchain-core", "langchain_community", "langchain-astradb", "langchain-openai", "pypdf", "python-dotenv"]
)