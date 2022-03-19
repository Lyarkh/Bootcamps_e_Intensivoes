from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pacman-jogo-teste",
    version="0.0.1",
    author="Lucas Emanuel",
    author_email="lcemanuel.emanuel@gmail.com",
    description="Recriando o jogo do pacman utilizando pygame",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lyarkh/Pacman",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)