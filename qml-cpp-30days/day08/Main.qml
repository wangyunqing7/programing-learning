import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 760
    height: 520
    visible: true
    title: "Day 08 - Signals"

    ColumnLayout {
        anchors.centerIn: parent
        width: 480
        spacing: 12

        TextField { id: input; Layout.fillWidth: true; placeholderText: "通知内容" }
        Button { Layout.fillWidth: true; text: "让 C++ 发信号"; onClicked: notifier.sendNotice(input.text) }
        TextArea {
            id: logText
            Layout.fillWidth: true
            Layout.preferredHeight: 220
            readOnly: true
            text: "通知日志\n"
        }
    }

    Connections {
        target: notifier
        function onNotice(message) {
            logText.text = message + "\n" + logText.text
        }
    }
}
