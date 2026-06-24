import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 500
    visible: true
    title: "Day 06 - QML calls C++"

    ColumnLayout {
        anchors.centerIn: parent
        width: 420
        spacing: 14

        Label { text: messageProvider.todayTopic(); font.pixelSize: 18 }
        TextField { id: nameField; Layout.fillWidth: true; placeholderText: "输入名字" }
        Button {
            Layout.fillWidth: true
            text: "调用 C++ greeting()"
            onClicked: output.text = messageProvider.greeting(nameField.text)
        }
        Label {
            id: output
            Layout.fillWidth: true
            text: "等待调用..."
            wrapMode: Text.WordWrap
            font.pixelSize: 20
        }
    }
}
