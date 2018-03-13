from conans import ConanFile
from conans import tools
import os

class glmConan(ConanFile):
    name = "glm"
    version = "0.9.8.5"
    license = "The Happy Bunny License, or the MIT License"
    url = "https://github.com/ulricheck/conan-glm"

    def source(self):
        tools.download("https://github.com/g-truc/glm/archive/%s.tar.gz" % self.version,
                       "glm.tar.gz")
        tools.unzip("glm.tar.gz")
        os.rename("glm-%s" % self.version, "source")
        os.unlink("glm.tar.gz")

    def package(self):
        self.copy("FindGLM.cmake", ".", ".")
        self.copy("*", dst="include/glm", src="glm/glm")
