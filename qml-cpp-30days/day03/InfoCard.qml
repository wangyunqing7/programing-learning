import QtQuick

Rectangle {
    id: root
    property string heading: "标题"
    property string body: "说明"
    property color accent: "#2563eb"

    width: 220
    height: 150
    radius: 12
    color: "white"
    border.color: "#dbe3ef"

    Column {
        anchors.fill: parent
        anchors.margins: 18
        spacing: 10

        Rectangle {
            width: 38
            height: 5
            radius: 3
            color: root.accent
        }

        Text {
            text: root.heading
            font.pixelSize: 20
            font.bold: true
            color: "#0f172a"
        }

        Text {
            width: parent.width
            text: root.body
            wrapMode: Text.WordWrap
            color: "#475569"
        }
    }
}
