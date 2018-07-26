[![Build Status](https://travis-ci.org/nicolastagliani/conan-tinyxml2.svg?branch=master)](https://travis-ci.org/nicolastagliani/conan-tinyxml2) [![Build status](https://ci.appveyor.com/api/projects/status/xcp120nf2ilk0a7n?svg=true)](https://ci.appveyor.com/project/nicolastagliani/conan-tinyxml2)

#conan-tinyxml2

[Conan](https://bintray.com/nicolastagliani/conan-tinyxml2/tinyxml2%3Anoname) package for TinyXML2 library made by Lee Thomason.


## Basic setup
    
recipe is currently hosted on bintray but the plan is to make it move to conan-center so for the time being you need to add the remote

    $ conan remote add conan-tinyxml2 https://api.bintray.com/conan/nicolastagliani/conan-tinyxml2  

and then

    $ conan install tinyxml2/6.2.0@noname/stable
    
no pre-built package is currently provided so you mighy want to append --build tinyxml2 to the install command

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    tinyxml2/6.2.0@noname/stable

    [options]
    tinyxml2:shared=True # False
    
    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
