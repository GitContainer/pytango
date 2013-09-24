import os
import sys
import sipconfig

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "test.sbf"

# Get the SIP configuration information.
config = sipconfig.Configuration()

# Run SIP to generate the code.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file, "test.sip"]))

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file)

python_lib = "python{v[0]}.{v[1]}".format(v=sys.version_info)

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
makefile.extra_libs = [python_lib, "test"]

# see all undefined references
makefile.extra_lflags = ['-z defs']

# Generate the Makefile itself.
makefile.generate()