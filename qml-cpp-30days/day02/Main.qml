import QtQuick

Window {
    id: window
    width: 720
    height: 480
    visible: true
    title: "Day 02 - Binding"

    property int clickCount: 0

    Rectangle {
        anchors.fill: parent
        color: clickCount % 2 === 0 ? "#eff6ff" : "#f0fdf4"

        Rectangle {
            id: card
            width: 360
            height: 220
            radius: 16
            anchors.centerIn: parent
            color: "white"
            border.color: "#cbd5e1"

            Column {
                anchors.centerIn: parent
                spacing: 14

                Text {
                    text: "点击次数：" + window.clickCount
                    font.pixelSize: 30
                    font.bold: true
                    color: "#0f172a"
                }

                Text {
                    text: window.clickCount >= 5 ? "绑定正在自动更新" : "点击卡片试试看"
                    font.pixelSize: 18
                    color: "#64748b"
                }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: window.clickCount += 1
            }
        }
    }
}
