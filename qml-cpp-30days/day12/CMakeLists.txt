cmake_minimum_required(VERSION 3.21)
project(Day12 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 REQUIRED COMPONENTS Quick)
qt_standard_project_setup(REQUIRES 6.8)

qt_add_executable(appDay12
    main.cpp
TaskListModel.h
TaskListModel.cpp
)

qt_add_qml_module(appDay12
    URI Day12
    VERSION 1.0
    QML_FILES
        Main.qml
)

target_link_libraries(appDay12 PRIVATE Qt6::Quick)
