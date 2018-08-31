from conans import ConanFile, CMake, tools
import os

class Tinyxml2Conan(ConanFile):
    name = "tinyxml2"
    version = "6.2.0"
    license = "MIT"
    url = "https://github.com/nicolastagliani/conan-tinyxml2"
    description = "TinyXML2 is a simple, small, efficient, C++ XML parser that can be easily integrated into other programs."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    source_dir = "tinyxml2"

    def source(self):
        self.run("git clone https://github.com/leethomason/tinyxml2.git {0}".format(self.source_dir))
        self.run("cd {0} && git checkout {1}".format(self.source_dir, self.version))
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("{0}/CMakeLists.txt".format(self.source_dir), "project(tinyxml2)",
                              '''project(tinyxml2)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = False
        if not self.options.shared:
            cmake.definitions["BUILD_STATIC_LIBS"] = True

        cmake.configure(source_folder=self.source_dir)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=self.source_dir)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        # Extract the license from header file
        header_file = os.path.join(self.source_folder, self.source_dir, "tinyxml2.h")
        header_content = tools.load(header_file)
        license_contents = header_content[2:header_content.find("*/",1)]
        tools.save("LICENSE", license_contents)

        # package the license file
        self.copy("license", dst="licenses", ignore_case=True, keep_path=False)

    def package_info(self):
        if not self.settings.build_type == "Debug":
            self.cpp_info.libs = ["tinyxml2"]
        else:
            self.cpp_info.libs = ["tinyxml2d"]
