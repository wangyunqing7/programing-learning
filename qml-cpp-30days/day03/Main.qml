import QtQuick

Window {
    width: 820
    height: 480
    visible: true
    title: "Day 03 - Components"

    Rectangle {
        anchors.fill: parent
        color: "#f8fafc"

        Column {
            anchors.centerIn: parent
            spacing: 24

            Text {
                text: "把界面拆成组件"
                font.pixelSize: 32
                font.bold: true
                color: "#0f172a"
            }

            Row {
                spacing: 18
                InfoCard { heading: "QML"; body: "描述界面结构"; accent: "#2563eb" }
                InfoCard { heading: "C++"; body: "承载数据和规则"; accent: "#16a34a" }
                InfoCard { heading: "CMake"; body: "组织项目构建"; accent: "#ea580c" }
            }
        }
    }
}
