import QtQuick
import QtQuick.Controls

Window {
    width: 1000
    height: 700
    visible: true
    title: qsTr("IFR Simulator")

    Grid {
        id: panel

        anchors.fill: parent
        rows: 2
        columns: 2

        AttitudeIndicator {
            id: horizon

            width: parent.width / panel.columns
            height: parent.height / panel.rows

            pitch: 2 * (stick1.y - controller1.height/2) / controller1.height
            roll: 360 * (stick1.x - controller1.width/2) / controller1.width
        }

        Altimeter {
            id: altimeter

            width: parent.width / panel.columns
            height: parent.height / panel.rows

            pressure: pressure_slider.value

            hundreds: altitude_slider.value * 100
            thousands: altitude_slider.value * 10
            ten_thousands: altitude_slider.value
        }

        HeadingIndicator {
            id: hsi

            width: parent.width / panel.columns
            height: parent.height / panel.rows

            heading: heading_slider.value

            onHeadingChanged: {
                console.log("Heading: " + heading)
            }
        }

        Column {
            width: parent.width / panel.columns
            height: parent.height / panel.columns

            Slider {
                id: pressure_slider

                anchors.left: parent.left
                anchors.right: parent.right

                from: 932
                value: 1013
                to: 1067
            }
            Slider {
                id: altitude_slider

                anchors.left: parent.left
                anchors.right: parent.right

                from: 0
                value: 1.235
                to: 2
            }
            Slider {
                id: heading_slider

                anchors.left: parent.left
                anchors.right: parent.right

                from: 0
                value: 23
                to: 360

                stepSize: 1
            }

            Rectangle {
                id: controller1

                width: parent.width
                height: parent.height/2

                color: "grey"

                MouseArea {
                    anchors.fill: parent

                    drag { target: stick1; axis: Drag.XAndYAxis; smoothed: false }

                    Rectangle {
                        id: stick1

                        width: 30
                        height: 30

                        x: parent.width / 2
                        y: parent.height / 2

                        color: "black"
                        radius: width / 2
                    }
                }
            }
        }
    }
}
