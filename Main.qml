import QtQuick

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

            pitch: 2 * (stick.y - controller.height/2) / controller.height
            roll: 360 * (stick.x - controller.width/2) / controller.width
        }

        Altimeter {
            id: altimeter

            width: parent.width / panel.columns
            height: parent.height / panel.rows
        }

        Rectangle {
            id: controller

            width: parent.width / panel.columns
            height: parent.height / panel.rows

            color: "grey"

            MouseArea {
                anchors.fill: parent

                drag { target: stick; axis: Drag.XAndYAxis; smoothed: false }

                Rectangle {
                    id: stick

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
