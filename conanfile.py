from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain
from conan.tools.files import rmdir, rm, collect_libs
import os


required_conan_version = ">=2.0"


class OggConan(ConanFile):
    name = "ogg"
    version = "1.3.5"
    python_requires = "aleya-conan-base/1.3.0@aleya/public"
    python_requires_extend = "aleya-conan-base.AleyaConanBase"
    ignore_cpp_standard = True

    exports_sources = "source/*"

    options = {
        "shared": [False, True],
        "fPIC": [False, True]
    }

    default_options = {
        "shared": False,
        "fPIC": True
    }

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["BUILD_SHARED_LIBS"] = self.options.shared
        tc.variables["BUILD_TESTING"] = False
        tc.variables["INSTALL_DOCS"] = False
        tc.variables["INSTALL_PKG_CONFIG_MODULE"] = False
        tc.variables["INSTALL_CMAKE_PACKAGE_MODULE"] = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "Ogg")
        self.cpp_info.set_property("cmake_target_name", "Ogg::ogg")
        self.cpp_info.set_property("pkg_config_name", "ogg")

        self.cpp_info.libs = collect_libs(self)
