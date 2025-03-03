cmake_minimum_required(VERSION 3.16)

project(ifrSimulator VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Quick)

qt_standard_project_setup(REQUIRES 6.5)

qt_add_executable(appifrSimulator
    main.cpp
)

qt_add_qml_module(appifrSimulator
    URI ifrSimulator
    VERSION 1.0
    QML_FILES
        Main.qml
	QML_FILES AttitudeIndicator.qml
	QML_FILES VerticalScrollImage.qml
	QML_FILES Altimeter.qml

        RESOURCES attitude_fg.png attitude_bg.png
        RESOURCES generator.py altimeter.svg.py
        RESOURCES altimeter_bg.svg attitude_fg.svg altimeter_hand1.svg altimeter_hand2.svg altimeter_hand3.svg altimeter_prss.svg
)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
set_target_properties(appifrSimulator PROPERTIES
#    MACOSX_BUNDLE_GUI_IDENTIFIER com.example.appifrSimulator
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

target_link_libraries(appifrSimulator
    PRIVATE Qt6::Quick
)

include(GNUInstallDirs)
install(TARGETS appifrSimulator
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)
