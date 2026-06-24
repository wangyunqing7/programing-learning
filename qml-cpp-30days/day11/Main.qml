import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 520
    visible: true
    title: "Day 11 - QStringListModel"

    ListView {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 8
        model: topicModel
        delegate: Rectangle {
            width: ListView.view.width
            height: 54
            radius: 10
            color: "#f8fafc"
            border.color: "#dbe3ef"
            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.leftMargin: 16
                text: model.display
                font.pixelSize: 18
            }
        }
    }
}
