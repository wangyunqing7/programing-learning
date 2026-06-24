cmake_minimum_required(VERSION 3.21)
project(Day26 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 REQUIRED COMPONENTS Quick)
qt_standard_project_setup(REQUIRES 6.8)

qt_add_executable(appDay26
    main.cpp
TaskModel.h
TaskModel.cpp
)

qt_add_qml_module(appDay26
    URI Day26
    VERSION 1.0
    QML_FILES
        Main.qml
)

target_link_libraries(appDay26 PRIVATE Qt6::Quick)
