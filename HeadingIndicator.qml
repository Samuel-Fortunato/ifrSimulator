import QtQuick

Item {
    id: root

    property real heading: 23
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

        Image {
            source: "svg/hsi_bg.svg"

            anchors.fill: parent

            rotation: -heading
        }

        Image {
            source: "svg/hsi_fg.svg"

            anchors.fill: parent
        }
    }
}
