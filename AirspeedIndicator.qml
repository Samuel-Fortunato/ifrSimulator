import QtQuick

Item {
    id: root

    readonly property int size: { Math.min( width, height ) }

    Item {
        id: square_frame

        width: size
        height: size

        anchors.centerIn: parent

        clip: true

        Image {
            source: "svg/airspeed_indicator_bg.svg"

            anchors.fill: parent
        }
    }
}
