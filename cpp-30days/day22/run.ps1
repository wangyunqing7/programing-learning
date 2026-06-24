New-Item -ItemType Directory -Force build | Out-Null
& "C:\Qt\Tools\mingw1310_64\bin\g++.exe" -std=c++17 -Wall -Wextra .\main.cpp -o .\build\cpp_day22.exe
& .\build\cpp_day22.exe
