import QtQuick
import QtQuick.Controls

Window {
    width: 500
    height: 600
    visible: true
    title: qsTr("Hello World")

    AttitudeIndicator {
        id: horizon

        size: { Math.min( parent.width, parent.height ) }
        anchors.horizontalCenter: parent.horizontalCenter

        pitch: horizonPitch.value
    }

    Slider {
        id: horizonPitch

        width: parent.width

        from: -1
        value: 0
        to: 1
    }
}
