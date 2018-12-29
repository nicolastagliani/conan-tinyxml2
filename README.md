[![Build Status](https://travis-ci.org/nicolastagliani/conan-tinyxml2.svg?branch=master)](https://travis-ci.org/nicolastagliani/conan-tinyxml2) 
[![Build status](https://ci.appveyor.com/api/projects/status/xcp120nf2ilk0a7n?svg=true)](https://ci.appveyor.com/project/nicolastagliani/conan-tinyxml2)
# conan-tinyxml2

[Conan](https://bintray.com/nicolastagliani/conan-tinyxml2/tinyxml2%3Anicolastagliani) package for [TinyXML2](https://github.com/leethomason/tinyxml2) library made by Lee Thomason.


## Basic setup
    
Recipe is hosted on my personal bintray and it's included also in conan center. Since conan-center is configured by default in conan installation you should be able to get the library just by installing it:

    $ conan install tinyxml2/7.0.1@nicolastagliani/stable 
    
## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    tinyxml2/7.0.1@nicolastagliani/stable

    [options]
    tinyxml2:shared=True # False
    
    [generators]
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the 
paths and variables that you need to link with your dependencies.
