import QtQuick

Item {
    id: root

    property alias pitch: bg.scroll
    property real roll: 0
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
            id: bg
            source: "attitude_bg.png"

            rotation: -roll

            anchors.fill: parent
        }

        Image {
            id: fg
            source: "attitude_fg.svg"

            anchors.fill: parent
        }
    }
}
