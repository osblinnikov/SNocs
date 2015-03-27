import os.path
import sys
import string

def prepare_mingw(env):
    env['TOOLS'] = ['mingw']
    env['CPPPATH'].extend([])
    env['CPPDEFINES'].extend([])
    env['LIBPATH'].extend([])
    if env['PLATFORM'] == 'x86':
        env['CCFLAGS'].extend(['-m32'])
        env['LINKFLAGS'].extend(['-m32'])
    elif env['PLATFORM'] == 'x64':
        env['CCFLAGS'].extend(['-m64'])
        env['LINKFLAGS'].extend(['-m64'])
    else:
        print "Unknown platform: "+env['PLATFORM']
        exit()
    if env['CONFIGURATION'] == 'Debug':
        env['CCFLAGS'].extend(['-g'])
    return env