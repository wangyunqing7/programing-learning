New-Item -ItemType Directory -Force build | Out-Null
& "C:\Qt\Tools\mingw1310_64\bin\gcc.exe" -std=c11 -Wall -Wextra .\main.c -o .\build\c_day21.exe
& .\build\c_day21.exe
