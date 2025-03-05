import QtQuick

Item {
    id: root

    property real altitude: 0
    property real pressure: 1013.2
    readonly property int size: { Math.min( width, height ) }

    implicitWidth: 100
    implicitHeight: 100
    width: implicitWidth
    height: implicitHeight

    Item {
        id: square_frame

        width: size
        height: size

        anchors.centerIn: parent

        clip: true

        VerticalScrollImage {
            source: "svg/altimeter/altimeter_prss.svg"

            x: (3/4) * square_frame.width
            y: square_frame.height / 2 - height / 2 + square_frame.height / 64

            width: square_frame.width * (1/8)
            height: (3/4) * width

            scroll: pressure
        }

        Image {
            id: bg

            source: "svg/altimeter/altimeter_bg.svg"

            anchors.fill: parent
        }
    }
}
