#this setup.py file we used to create the setup of project (all the information of project present in it)
#were all the details present in this project futhur these file we can used as package  for other projectss

#importing all the important library to create setup file
from setuptools import setup,find_packages
from typing import List



#now creating user defined function of get_requirements!!
def get_requirements(filename:str)->list[str]:
    with open(filename,'r') as f:
        #reading all the content from text file rtn the result into list object
        lines = f.read().split('\n')
        requirement = []
        #now checking this trigger command -e . present in text file or not 
        for line in lines:
            if '-e .' == line:
                requirement.append(line.strip('-e .'))
            else:
                requirement.append(line.strip())

    return requirement



#now creating the setup class object and passing all the information of project present in it
setup(
    name = 'ML_AUTOMOBILE', #name of the project
    version='0.0.1',
    long_description=open('README.md').read(),
    author="Raees Azam Shaikh",
    author_email='shaikhraishazam@gmail.com',
    url='https://github.com/raish123/ML_AUTOMOBILE/' ,# use the URL to the github repo
    packages= find_packages(),  #creating an object of find_packages class is powerful class will help to install all the library used in this project
    install_requires = get_requirements('requirements.txt')

)

