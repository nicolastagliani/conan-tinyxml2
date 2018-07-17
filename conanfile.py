from conans import ConanFile, CMake, tools


class Tinyxml2Conan(ConanFile):
    name = "tinyxml2"
    version = "6.2.0"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "TinyXML2 is a simple, small, efficient, C++ XML parser that can be easily integrated into other programs."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/leethomason/tinyxml2.git")
        self.run("cd tinyxml2 && git checkout {0}".format(self.version))
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("tinyxml2/CMakeLists.txt", "project(tinyxml2)",
                              '''project(tinyxml2)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        if self.options.shared:
            cmake.definitions["BUILD_SHARED_LIBS"] = True
        else:
            cmake.definitions["BUILD_STATIC_LIBS"] = True
        cmake.configure(source_folder="tinyxml2")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="tinyxml2")
        self.copy("*tinyxml2.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["tinyxml2"]
