from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    Returns:
        List[str]: _description_
    """
    requirement_list:List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("Requirements file not found")
        
    return requirement_list

setup(
    name="NetWorkSecurity",
    version="0.0.0.1",
    description="A network security package for cyber security learning",
    author="Rupayan Dey",
    author_email="rupayandey134@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)