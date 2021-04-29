from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='quant_cuda',
    ext_modules=[
        CUDAExtension('quant_cuda', [
            "quant_cuda.cpp",
            "bit_helper.cu",
            "sim_helper.cu",
            "block_kernel.cu",
            "float_kernel.cu",
            "fixed_point_kernel.cu",
            "quant.cu",
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
