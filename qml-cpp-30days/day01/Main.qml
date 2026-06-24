import QtQuick

Window {
    width: 720
    height: 480
    visible: true
    title: "Day 01 - Hello QML"

    Rectangle {
        anchors.fill: parent
        color: "#f8fafc"

        Column {
            anchors.centerIn: parent
            spacing: 14

            Text {
                text: "Hello QML"
                font.pixelSize: 40
                font.bold: true
                color: "#0f172a"
            }

            Text {
                text: "这是第一个由 C++ 加载的 Qt Quick 窗口"
                font.pixelSize: 18
                color: "#475569"
            }
        }
    }
}
