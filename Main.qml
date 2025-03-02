import QtQuick
import QtQuick.Controls

Window {
    width: 300
    height: 600
    visible: true
    title: qsTr("IFR Simulator")



    Column {
        anchors.fill: parent

        AttitudeIndicator {
            id: horizon

            size: 300

            pitch: 2 * (stick.y - height/2) / height
            roll: 360 * (stick.x - width/2) / width
        }

        Rectangle {
            width: 300
            height: 300

            color: "grey"

            MouseArea {
                anchors.fill: parent

                drag { target: stick; axis: Drag.XAndYAxis; smoothed: false }

                Rectangle {
                    id: stick

                    width: 30
                    height: 30

                    x: 150
                    y: 150

                    color: "black"
                    radius: width / 2
                }
            }
        }
    }
}
