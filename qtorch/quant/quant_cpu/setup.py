from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name='quant_cpu',
    ext_modules=[
        CppExtension('quant_cpu', [
            "quant_cpu.cpp",
            "bit_helper.cpp",
            "sim_helper.cpp",
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
