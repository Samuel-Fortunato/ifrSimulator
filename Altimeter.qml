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

    Image {
        id: bg


        anchors.fill: parent
    }
}
