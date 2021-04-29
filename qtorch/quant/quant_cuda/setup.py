from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='quant_cuda',
    ext_modules=[
        CUDAExtension('quant_cuda', [
            "quant_cuda/quant_cuda.cpp",
            "quant_cuda/bit_helper.cu",
            "quant_cuda/sim_helper.cu",
            "quant_cuda/block_kernel.cu",
            "quant_cuda/float_kernel.cu",
            "quant_cuda/fixed_point_kernel.cu",
            "quant_cuda/quant.cu",
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
