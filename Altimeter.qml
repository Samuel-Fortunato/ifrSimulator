import QtQuick

Item {
    id: root

    readonly property int size: { Math.min( width, height ) }
    property real pressure: 1013.2
    property real hundreds: 1.5
    property real thousands: 4
    property real ten_thousands: 1

    Item {
        id: prss_const

        readonly property real factor: 2/(932 - 1067)
        readonly property real bias: 1 + 2 *(932/(1067 - 932))
    }

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
            source: "svg/altimeter_prss.svg"

            x: (3/4) * square_frame.width
            y: square_frame.height / 2 - height / 2 + square_frame.height / 64

            width: square_frame.width * (1/8)
            height: (3/4) * width

            scroll:  pressure * prss_const.factor + prss_const.bias
        }

        Image {
            id: bg

            source: "svg/altimeter_bg.svg"

            anchors.fill: parent
        }

        Image {
            id: hand1
            source: "svg/altimeter_hand1.svg"

            anchors.fill: parent

            rotation: hundreds * (360/10)
        }

        Image {
            id: hand2
            source: "svg/altimeter_hand2.svg"

            anchors.fill: parent

            rotation: thousands * (360/10)
        }

        Image {
            id: hand3
            source: "svg/altimeter_hand3.svg"

            anchors.fill: parent

            rotation: ten_thousands * (360/10)
        }
    }
}
