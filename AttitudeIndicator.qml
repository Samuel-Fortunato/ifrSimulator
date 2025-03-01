import QtQuick

Item {
    id: root

    property alias size: root.width
    property real pitch: 0

    implicitWidth: 100
    width: implicitWidth
    height: width
    clip: true

    VerticalScrollImage {
        id: bg
        source: "attitude_bg.png"

        frame: root
    }

    Image {
        id: fg
        source: "attitude_fg.png"

        anchors.fill: root
    }
}
