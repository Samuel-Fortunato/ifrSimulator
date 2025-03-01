import QtQuick

Image {
    id: root

    required property QtObject frame
    required source

    property int center: (frame.height - height) / 2
    property bool scrollable: (height > frame.height)
    property int maxScroll: (height - frame.height) / 2

    function __calculateScrollY() {
        if (!scrollable) {
            return center
        }

        return center + (maxScroll * pitch)
    }

    anchors.horizontalCenter: frame.horizontalCenter
    width: frame.width
    height: implicitHeight * (width / implicitWidth) // Maintain aspect ratio

    y: __calculateScrollY()
}
