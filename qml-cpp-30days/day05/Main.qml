import QtQuick

Window {
    width: 780
    height: 520
    visible: true
    title: "Day 05 - States"

    Rectangle {
        anchors.fill: parent
        color: "#f8fafc"

        Rectangle {
            id: card
            property bool expanded: false

            width: 340
            height: 180
            radius: 18
            anchors.centerIn: parent
            color: "#dbeafe"

            Column {
                anchors.centerIn: parent
                spacing: 10

                Text {
                    text: card.expanded ? "展开状态" : "普通状态"
                    font.pixelSize: 30
                    font.bold: true
                    color: "#0f172a"
                }

                Text {
                    text: "点击卡片切换状态"
                    font.pixelSize: 17
                    color: "#475569"
                }
            }

            MouseArea {
                anchors.fill: parent
                onClicked: card.expanded = !card.expanded
            }

            states: State {
                name: "expanded"
                when: card.expanded
                PropertyChanges { target: card; width: 520; height: 300; color: "#dcfce7" }
            }

            transitions: Transition {
                NumberAnimation { properties: "width,height"; duration: 260; easing.type: Easing.OutCubic }
                ColorAnimation { duration: 260 }
            }
        }
    }
}
