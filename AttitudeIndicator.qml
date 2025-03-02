import QtQuick

Item {
    id: root

    property alias size: root.width
    property alias pitch: bg.scroll
    property real roll: 0

    implicitWidth: 100
    width: implicitWidth
    height: width
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

        anchors.fill: root
    }
}
