import sys; 
print("python version ="+sys.version)

import pydantic_core as _; 
print(_.__path__)

#ImportError: dlopen(/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pydantic_core/_pydantic_core.cpython-312-darwin.so, 0x0002): tried: '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pydantic_core/_pydantic_core.cpython-312-darwin.so' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/System/Volumes/Preboot/Cryptexes/OS/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pydantic_core/_pydantic_core.cpython-312-darwin.so' (no such file), '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pydantic_core/_pydantic_core.cpython-312-darwin.so' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64'))


"""
python test_packages.py
python version =3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)]
['/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pydantic_core']
"""