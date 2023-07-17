from setuptools import setup, find_packages

setup(
  name = 'pegasusX',
  packages = find_packages(exclude=[]),
  version = '0.3.1',
  license='MIT',
  description = 'pegasus - Pytorch',
  author = 'Kye Gomez',
  author_email = 'kye@apac.ai',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/kyegomez/pegasus',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'optimizers',
    "Prompt Engineering"
  ],
  install_requires=[
    'hnswlib==0.7.0',
    'pandas==1.3.5',
    'pydantic==1.9.0',
    'requests==2.28.1',
    'typing_extensions==4.5.0',
    'uvicorn[standard]==0.18.3',
    'torch',
    'torchvision',
    'torchaudio',
    'timm==0.6.7',
    'pytorchvideo',
    'ftfy',
    'regex',
    'einops',
    'fvcore',
    'decord==0.6.0',
    'numba',
    'joblib',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)