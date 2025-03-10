cmake_minimum_required(VERSION 3.16)

project(ifrSimulator VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Quick)
find_package(Python REQUIRED COMPONENTS Interpreter)

qt_standard_project_setup(REQUIRES 6.5)

qt_add_executable(appifrSimulator
    main.cpp
)

set(SVG_DIRECTORY svg)
set(SVG_GENERATOR ${SVG_DIRECTORY}/generator.py)
set(SVG_RESOURCES
    ${SVG_DIRECTORY}/constants.py
    ${SVG_DIRECTORY}/color_palette.py
)
set(SVG_SCRIPTS
    ${SVG_DIRECTORY}/altimeter_bg.svg.py
    ${SVG_DIRECTORY}/altimeter_prss.svg.py
    ${SVG_DIRECTORY}/altimeter_hand1.svg.py
    ${SVG_DIRECTORY}/altimeter_hand2.svg.py
    ${SVG_DIRECTORY}/altimeter_hand3.svg.py

    ${SVG_DIRECTORY}/hsi_bg.svg.py
    ${SVG_DIRECTORY}/hsi_fg.svg.py
)
set(SVG_FILES "")

foreach(SCRIPT ${SVG_SCRIPTS})
    # Extract filename without extension
    get_filename_component(FILE_NO_PY ${SCRIPT} NAME_WLE)
    get_filename_component(FILE_DIR ${SCRIPT} PATH)

    # Define output SVG file
    set(SVG_FILE ${FILE_DIR}/${FILE_NO_PY})

    # Append to resources list
    list(APPEND SVG_FILES ${SVG_FILE})

    # Add a custom target for each SVG
    add_custom_command(
        OUTPUT ${SVG_FILE}
        COMMAND ${Python_EXECUTABLE} ${CMAKE_SOURCE_DIR}/${SVG_GENERATOR} -o ${CMAKE_SOURCE_DIR}/${SVG_FILE} ${CMAKE_SOURCE_DIR}/${SCRIPT}
        DEPENDS
            ${CMAKE_SOURCE_DIR}/${SVG_GENERATOR}
            ${CMAKE_SOURCE_DIR}/${SVG_RESOURCES}
            ${CMAKE_SOURCE_DIR}/${SCRIPT}
        COMMENT "Generating ${SVG_FILE} using ${SCRIPT}"
        VERBATIM
    )
endforeach()

add_custom_target(generate_svgs ALL DEPENDS ${SVG_FILES})

qt_add_qml_module(appifrSimulator
    URI ifrSimulator
    VERSION 1.0
    QML_FILES
        Main.qml
        AttitudeIndicator.qml
        VerticalScrollImage.qml
        Altimeter.qml

    RESOURCES
        attitude_fg.png attitude_bg.png attitude_fg.svg
        ${SVG_GENERATOR}
        ${SVG_RESOURCES}
        ${SVG_SCRIPTS}
        ${SVG_FILES}
        QML_FILES HeadingIndicator.qml
        RESOURCES svg/hsi_bg.svg.py
)

add_dependencies(appifrSimulator generate_svgs)

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
