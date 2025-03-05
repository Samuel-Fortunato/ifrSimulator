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

            hundreds: hundreds_slider.value
        }

        Rectangle {
            id: controller1

            width: parent.width / panel.columns
            height: parent.height / panel.rows

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

        Column {
            width: parent.width / panel.columns

            Slider {
                id: pressure_slider

                anchors.left: parent.left
                anchors.right: parent.right

                from: 932
                value: 1013
                to: 1067
            }
            Slider {
                id: hundreds_slider

                anchors.left: parent.left
                anchors.right: parent.right

                from: 0
                value: 1.5
                to: 10
            }
        }
    }
}
