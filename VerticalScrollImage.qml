import QtQuick

Item {
    id: root

    property alias source: image.source
    property real scroll: 0

    clip: true

    Image {
        id: image

        required source

        property int center: (root.height - height) / 2
        property bool scrollable: (height > root.height)
        property int maxScroll: (height - root.height) / 2 // Maximum pixels to scroll

        function __calculateScrollY() {
            if (!scrollable) {
                return center
            }

            return center + (maxScroll * scroll)
        }

        width: root.width
        height: implicitHeight * (width / implicitWidth) // Maintain aspect ratio

        anchors.horizontalCenter: root.horizontalCenter
        y: __calculateScrollY()
    }
}
